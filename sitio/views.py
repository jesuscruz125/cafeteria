from django.shortcuts import render, redirect
from .models import Producto, Evento, Sucursal, Comentario
from .forms import ComentarioForm


# Create your views here.

def inicio(request):
    productos = Producto.objects.filter(disponible=True)[:3]
    return render(request, 'home.html', {'productos': productos})

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})

def eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos.html', {'eventos': eventos})

def sucursales(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'sucursales.html', {'sucursales': sucursales})

def contacto(request):
    return render(request, 'contacto.html')

def comentarios(request):
    comentarios = Comentario.objects.filter(aprobado=True).order_by('-fecha')
    return render(request, 'comentarios.html', {'comentarios': comentarios})

def comentarios(request):
    comentarios = Comentario.objects.filter(aprobado=True).order_by('-fecha')

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('/comentarios/')
    else:
        form = ComentarioForm()

    return render(request, 'comentarios.html', {'comentarios': comentarios, 'form': form})
