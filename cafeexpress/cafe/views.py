from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from .models import Noticia
from .forms import ContactoForm
def inicio(request):
    return render(request,'cafe/inicio.html',{'noticias':Noticia.objects.order_by('-fecha')[:3]})
def nosotros(request): return render(request,'cafe/nosotros.html')
def noticias(request): return render(request,'cafe/noticias.html',{'noticias':Noticia.objects.order_by('-fecha')})
def noticia_detalle(request,pk): return render(request,'cafe/noticia_detalle.html',{'noticia':get_object_or_404(Noticia,pk=pk)})
def contacto(request):
    form=ContactoForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        form.save(); messages.success(request,'Tu mensaje fue enviado correctamente.'); return redirect('contacto')
    return render(request,'cafe/contacto.html',{'form':form})
