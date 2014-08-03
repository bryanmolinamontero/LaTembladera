# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
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
