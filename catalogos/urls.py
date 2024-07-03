from django.urls import path, include
from catalogos.views import *

urlpatterns = [
    path('',home,name="home"),
    path('nuestrasPlantas',nuestrasPlantas,name="nuestrasPlantas"),
    path('jardines',jardines,name="jardines"),
    path('cultivando',cultivando,name="cultivando"),
    path('contacto',contacto,name="contacto"),
    path('contactoRealizado',contacto,name="contact"),
    
    ]
