# Create your views here.
from django.shortcuts import render_to_response
from tembladera.models import *

def index(request):
    datos=Noticias.objects.all()
    return render_to_response('index.html', {"datos":datos})


def origen(request):
    return render_to_response('origen.html')