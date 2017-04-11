# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from django.template import RequestContext, Context
from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
import json


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
    
    sended = False
    message = None #"Erro ao enviar a mensagem ..!"
    
    if request.method == "POST":
        post = request.POST
        print(post)
        nome = request.POST["name"]
        email = post["email"]
        assunto = post["assunto"]
        fone = post["phone"]
        mensagem = post["message"]
        to='contatomotivagym@gmail.com', 
        from_email='contatomotivagym@gmail.com'
        try:
            ctx = {
                'nome': nome,
                'email': email,
                'assunto': assunto,
                'fone':fone,
                'mensagem': mensagem
            }
            message = get_template('gym/email.html').render(Context(ctx))
            msg = EmailMessage(assunto, message, to=to, from_email=from_email)
            msg.content_subtype = 'html'
            msg.send()
            resp = {"sended": True, "message": "Mensagem enviado com successo ..!"}
            return HttpResponse(status=200, content_type='application/json', content=json.dumps(resp))
            
        except Exception as ex:
            print (ex)
            resp = {"sended":False, "message":"Erro: Não foi possível enviar a ..!"}
            return HttpResponse(status=200, content_type='application/json', content=json.dumps(resp))       
        
    return render(request, "gym/contato.html")

def Programas(request):
    return render(request, "gym/programas.html")
    
def custom_404(request):
    return render_to_response("gym/404.html", RequestContext(request) )
    

    
