# Create your views here.
from django.core.mail import EmailMultiAlternatives
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from tembladera.models import *


def index(request):
    extraerNoticia=Noticias.objects.all().order_by("-id")
    paginator = Paginator(extraerNoticia, 1)
    page = request.GET.get('page')
    try:
        noticias = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        noticias = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        noticias = paginator.page(paginator.num_pages)
    return render_to_response('index.html', {"noticias":noticias})


def origen(request):
    return render_to_response('origen.html')


def misionYvision(request):
    return render_to_response('misionYvision.html')

def objetivos(request):
    return render_to_response('objetivos.html')

def politicas(request):
    return render_to_response('politicas.html')

def estructuraFuncional(request):
    return render_to_response('estructuraFuncional.html')

def productos(request):
    return render_to_response('productos.html')

def proyectos(request):
    extraerProyectos=Proyectos.objects.all().order_by("-id")
    paginator = Paginator(extraerProyectos, 3)
    page = request.GET.get('page')
    try:
        proyectos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        proyectos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        proyectos = paginator.page(paginator.num_pages)
    return render_to_response('proyectos.html', {"proyectos":proyectos})


def galeria(request):
    return render_to_response('galeria.html')

def florayfauna(request):
    return render_to_response('florayfauna.html')

def contacto(request):
    return render_to_response('contacto.html')

def verNoticia(request):
    return HttpResponseRedirect('/index/')

def ver_noticia(request, id_noticia):

    try:
        noticia = Noticias.objects.get(id=id_noticia)
        if request.method == 'GET':
            valores = Noticias.objects.all()
            return render_to_response('ver_noticia.html', RequestContext(request, locals()))
    except Exception:
        return HttpResponseRedirect('/')

def noticias(request):
    extraerNoticias=Noticias.objects.all().order_by("-id")
    paginator = Paginator(extraerNoticias, 5)
    page = request.GET.get('page')
    try:
        noticias = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        noticias = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        noticias = paginator.page(paginator.num_pages)
    return render_to_response('noticias.html', {"noticias":noticias})



emisor = "bryanux@hotmail.com"
destinatario = "bryanux@hotmail.com"


def enviarCorreo(request):
    if request.method=='POST':

        nombre =  request.POST['txtNombre']
        correo =  request.POST['txtCorreo']
        telefono =  request.POST['txtTelefono']
        mensaje =  request.POST['txtContenidoMensaje']

        subject = 'CONTACTO'
        text_content = 'Mensaje...nLinea 2nLinea3'

        html_content = '<b>' \
                       'ASOGROTEM </br></br>' \
                       'Nombres: %s </br></br>' \
                       'Correo: %s </br></br>' \
                       'Telefono: %s </br></br>' \
                       'Mensaje: %s </br></br>' \
                       '</b>' % (nombre , correo, telefono, mensaje)
        from_email = '"ASOGROTEM" <%s>' % emisor
        to = destinatario
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        return HttpResponseRedirect('/contacto/')
    else:
        return HttpResponseRedirect('/contacto/')



def enviarCorreo2(request):
    if request.method=='POST':

        nombre =  request.GET['nombre']
        correo =  request.GET['correo']
        telefono =  request.GET['telefono']
        mensaje =  request.GET['mensaje']

        subject = 'CONTACTO'
        text_content = 'Mensaje...nLinea 2nLinea3'

        html_content = '<b>' \
                       'ASOGROTEM </br></br>' \
                       'Nombres: %s </br></br>' \
                       'Correo: %s </br></br>' \
                       'Telefono: %s </br></br>' \
                       'Mensaje: %s </br></br>' \
                       '</b>' % (nombre , correo, telefono, mensaje)
        from_email = '"ASOGROTEM" <%s>' % emisor
        to = destinatario
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        return HttpResponse("SU MENSAJE HA SIDO ENVIADO")
    else:
        return HttpResponseRedirect('/contacto/')