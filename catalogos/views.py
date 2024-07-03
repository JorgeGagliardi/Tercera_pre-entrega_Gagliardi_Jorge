from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request,"catalogos/index.html")

def nuestrasPlantas(request):
    contexto = {"plantas": Plantas.objects.all()}
    return render(request,"catalogos/nuestrasPlantas.html", contexto)

def jardines(request):
    return render(request,"catalogos/jardines.html")

def cultivando(request):
    return render(request,"catalogos/cultivando.html")

def contacto(request):
    return render(request,"catalogos/contacto.html")

def contacto(request):
    if request.method=="POST":
        miForm = Contacto(request.POST)
        if miForm.is_valid():
            contacto_apellido = miForm.cleaned_data.get("apellido")
            contacto_ciudad = miForm.cleaned_data.get("ciudad")
            contacto_pais = miForm.cleaned_data.get("pais")
            contacto_correo = miForm.cleaned_data.get("correo")
            contacto_telefono = miForm.cleaned_data.get("telefono")
            contacto_mensaje = miForm.cleaned_data.get("mensaje")
            contactos = Contactos(apellido=contacto_apellido,
                                ciudad=contacto_ciudad,
                                pais=contacto_pais,
                                correo=contacto_correo,
                                telefono=contacto_telefono,
                                mensaje=contacto_mensaje)
            contactos.save()
            contexto = {"contactos":Contactos.objects.all()}
            return render(request,"catalogos/contactoRealizado.html",contexto)
    else:
        miForm = Contacto()
        return render(request,"catalogos/contacto.html",{"form":miForm})
    