from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PostearForm
from Blog.models import Postear

# Create your views here.
def inicio(request):
    return render(request, "Blog/index.html")

def postearForm(request):
    if request.method == 'POST':
        miFormulario = postearForm(request.POST) 
        print(miFormulario)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            info = Postear(titulo = info['titulo'], autor = info['autor'], contenido = info['contenido'])
            info.save()
            return render(request, 'Blog/index.html')
    else:
        miFormulario = postearForm()
    return render(request, "Blog/postearForm.html",{'miFormulario':miFormulario})