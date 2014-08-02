# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
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


def misionYvision(request):
    return render_to_response('misionYvision.html')


def origen(request):
    return render_to_response('origen.html')