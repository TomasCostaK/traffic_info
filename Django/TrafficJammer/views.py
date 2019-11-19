from django.http import HttpResponse
from django.shortcuts import render
import json
from TrafficJammer.models import Street,Section,Transit,Acidente,SectionSerializer,StreetSerializer
# Create your views here.


def info(request):
    if request.method=="GET":
        return HttpResponse(json.dumps(SectionSerializer(Section.objects.all(),many=True).data))
