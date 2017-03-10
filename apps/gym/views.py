from django.shortcuts import render

# Create your views here.

def Index(request):
    return render(request, "gym/index.html")

def Aulas(request):
    return render(request, "gym/aulas.html")

def Treinador(request):
    return render(request, "gym/trainer.html")
    
def Sobre(request):
    return render(request, "gym/about.html")

def Contato(request):
    return render(request, "gym/contato.html")

def Programas(request):
    return render(request, "gym/programas.html")