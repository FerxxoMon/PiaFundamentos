from django import forms
from .models import MensajeContacto
class ContactoForm(forms.ModelForm):
    class Meta:
        model=MensajeContacto
        fields=['nombre','correo','asunto','mensaje']
        widgets={f:forms.TextInput(attrs={'class':'form-control'}) for f in ['nombre','correo','asunto']}
        widgets['mensaje']=forms.Textarea(attrs={'class':'form-control','rows':5})
