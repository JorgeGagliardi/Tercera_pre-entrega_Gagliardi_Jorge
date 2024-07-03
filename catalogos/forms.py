from django import forms

class Contacto(forms.Form):
    apellido = forms.CharField(max_length=50, required=True)
    ciudad   = forms.CharField(max_length=50, required=True)
    pais     = forms.CharField(max_length=50, required=True, label="País")
    correo   = forms.CharField(max_length=50, required=True)
    telefono = forms.CharField(max_length=50, required=True, label="Teléfono")
    mensaje  = forms.CharField(max_length=240, required=True)
