from django.contrib import admin
from .models import Noticia, MensajeContacto
@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin): list_display=('titulo','fecha')
@admin.register(MensajeContacto)
class MensajeAdmin(admin.ModelAdmin): list_display=('nombre','correo','asunto','fecha')
