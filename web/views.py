from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Flan, ContactForm
from .forms import ContactFormModelForm
from django.contrib.auth.decorators import login_required


def indice (request):
    flanes_publicos = Flan.objects.filter(is_private=False)

    return render(request, 'index.html', {
        'flanes_publicos': flanes_publicos
    })

def acerca(request):
    return render(request, 'about.html',{})

@login_required
def bienvenido(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html',{ 'flanes_privados' : flanes_privados })

def contacto(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/exito')
    else:
        form = ContactFormModelForm()

    return render(request, 'contactus.html', {'form': form})

def exito(request):
    return render(request, 'success.html', {})