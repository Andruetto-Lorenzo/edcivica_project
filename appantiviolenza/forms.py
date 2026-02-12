from django import forms
from .models import Utente

class UtenteForm(forms.ModelForm):
    class Meta:
        model = Utente
        fields = ['nome_utente', 'email', 'password', 'telefono', 'regione_provenienza', 'fascia_eta']
        