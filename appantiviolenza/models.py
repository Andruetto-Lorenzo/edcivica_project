from django.db import models

class Operatore(models.Model):
    specializzazione = models.CharField(max_length=50, null=False, blank=True)
    id_operatore = models.BigAutoField(primary_key=True)
    turno_inizio = models.TimeField(null=True, blank=True)
    turno_fine = models.TimeField(null=True, blank=True)

class Ticket(models.Model):
    VIOLENZA_CHOICES = [
        ('fisica', 'fisica'),
        ('psicologica', 'psicologica'),
        ('stalking', 'stalking'),
    ]

    STATO_RICHIESTA_CHOICES = [
        ('open', 'Aperta'),
        ('in carico', 'In carico'),
        ('closed', 'Chiusa'),
        ('Fake alarm', 'Falso allarme'),
    ]

    LIVELLO_URGENZA_CHOICES = [
        ('low', 'Basso'),
        ('medium', 'Medio'),
        ('high', 'Alto'),
    ]

    FASCE_ETA_CHOICES = [
        ('-18', 'Minorenne'),
        ('18-29', '18-29'),
        ('30-49', '30-49'),
        ('50-70', '50-70'),
        ('70+', '70+'),
    ]

    nome_utente = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    telefono = models.BigIntegerField(null=False, blank=False)
    regione_provenienza = models.CharField(max_length=20, null=False, blank=False)
    fascia_eta = models.CharField(max_length=10, choices=FASCE_ETA_CHOICES)
    data = models.DateField(null=False, blank=False, auto_now_add=True)
    ora = models.TimeField(null=False, blank=False, auto_now_add=True)
    tipo_violenza = models.CharField(max_length=15, choices=VIOLENZA_CHOICES, null=False, blank=False)
    descrizione = models.CharField(max_length=500, null=False, blank=False)
    livello_urgenza = models.IntegerField(null=False, blank=False, choices=LIVELLO_URGENZA_CHOICES)
    stato_richiesta = models.CharField(max_length=20, null=False, blank=False)

class Segnalazioni(models.Model):
    id_richiesta = models.BigAutoField(primary_key=True)
    azione_intrapresa = models.CharField(max_length=20, null=False, blank=False)
    esito = models.CharField(max_length=20, null=False, blank=False)
    note_riservate = models.CharField(max_length=100, null=False, blank=False)
