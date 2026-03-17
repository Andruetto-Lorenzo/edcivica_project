# from django.shortcuts import render
# from ..models import Ticket

# def operator_view(request):
#     tickets = Ticket.objects.all()
#     # ticket.stato_richiesta = "In carico"
#     # ticket.save()

#     if request.method == 'POST':
#         btn_accetta = request.POST.get("btn_accetta")
#         if btn_accetta == 'Aperta':
#             btn_accetta = 'In carico'
#         else:
#             btn_accetta = 'Chiusa'

#         print(btn_accetta)

#     print(tickets[0].stato_richiesta)

#     return render(request, 'operator.html', {
#         'tickets': tickets,
#     })

# def change_state_tickets(request):
#     ticket = request.POST.get("btn_accetta")
#     print(ticket)


from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from ..models import Ticket
import psycopg2
import psycopg2.extras  # per RealDictCursor
 
def _get_connection():
    """Apre una connessione psycopg2 usando le stesse credenziali di settings.py."""
    db = settings.DATABASES['default']
    return psycopg2.connect(
        dbname=db['NAME'],
        user=db['USER'],
        password=db['PASSWORD'],
        host=db.get('HOST', 'localhost'),
        port=db.get('PORT', '5432'),
    )
 
def operator_view(request):
    if request.method == 'POST':
        ticket_id = request.POST.get("ticket_id")
        azione    = request.POST.get("azione")
        ticket    = get_object_or_404(Ticket, pk=ticket_id)
 
        if azione == 'accetta' and ticket.stato_richiesta == 'Aperta':
            ticket.stato_richiesta = 'In carico'
            ticket.save()
        elif azione == 'chiudi' and ticket.stato_richiesta == 'In carico':
            ticket.stato_richiesta = 'Chiusa'
            ticket.save()
        elif azione == 'fake' and ticket.stato_richiesta == 'In carico':
            ticket.stato_richiesta = 'Fake alarm'
            ticket.save()
 
        return redirect('operator_space')
 
    ordina = request.GET.get('ordina', 'urgenza')
 
    conn = _get_connection()
    try:
        # RealDictCursor restituisce ogni riga come dizionario {colonna: valore}
        # così nel template possiamo usare {{ t.nome_utente }}, {{ t.data }}, ecc.
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
 
            if ordina == 'data':
                cur.execute("""
                    SELECT id, nome_utente, regione_provenienza, tipo_violenza,
                           livello_urgenza, data, ora, stato_richiesta,
                           email, telefono, fascia_eta, descrizione
                    FROM   appantiviolenza_ticket
                    ORDER  BY data DESC, ora DESC
                """)
            else:
                cur.execute("""
                    SELECT id, nome_utente, regione_provenienza, tipo_violenza,
                           livello_urgenza, data, ora, stato_richiesta,
                           email, telefono, fascia_eta, descrizione
                    FROM   appantiviolenza_ticket
                    ORDER  BY
                        CASE livello_urgenza
                            WHEN 'high'   THEN 0
                            WHEN 'medium' THEN 1
                            WHEN 'low'    THEN 2
                            ELSE 9
                        END ASC,
                        data DESC,
                        ora  DESC
                """)
 
            tickets = cur.fetchall()
    finally:
        conn.close()
 
    return render(request, 'operator.html', {
        'tickets': tickets,
        'ordina':  ordina,
    })