from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Proyecto
from django.core.mail import send_mail

def pagina_principal(request):
    return render(request, 'portfolio_daniel_developer/pagina_principal.html')

def lista_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'portfolio_daniel_developer/lista_proyectos.html', {'proyectos': proyectos})

def sobre_mi(request):
    sobre_mi = sobre_mi.objects.all()
    return render(request, 'portfolio_daniel_developer/sobre_mi.html', {'sobre_mi': sobre_mi})

def contactame(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Procesar el formulario y enviar el correo
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']

            # Aquí se envía el correo
            send_mail(
                'Nuevo Mensaje desde Portafolio',
                f'Nombre: {nombre}\nEmail: {email}\nMensaje: {mensaje}',
                'dev.daniel.alcazar@outlook.com',
                ['dev.daniel.alcazar@gmail.com'],
                fail_silently=False,
            )

            # Puedes agregar lógica adicional aquí, por ejemplo, redirigir a una página de éxito.
            return redirect('nombre_de_la_ruta_de_la_pagina_de_exito')

    else:
        form = ContactForm()

    return render(request, 'portfolio_daniel_developer/pagina_principal.html', {'form': form})

def pagina_principal(request):
    form = ContactForm()  # O cualquier otra lógica relacionada con el formulario
    return render(request, 'portfolio_daniel_developer/pagina_principal.html', {'form': form})