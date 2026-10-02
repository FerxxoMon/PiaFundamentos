from django.urls import path
from . import views
urlpatterns=[path('',views.inicio,name='inicio'),path('nosotros/',views.nosotros,name='nosotros'),path('noticias/',views.noticias,name='noticias'),path('noticias/<int:pk>/',views.noticia_detalle,name='noticia_detalle'),path('contacto/',views.contacto,name='contacto')]
