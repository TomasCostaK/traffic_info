from django.http import HttpResponse
from django.shortcuts import render
import pika
import json
import math
from datetime import datetime,timezone,timedelta
from django.views.decorators.csrf import csrf_exempt

from TrafficJammer.models import Street, \
    Section, \
    Transit, \
    Accident, \
    SectionSerializer, \
    StreetSerializer, \
    StreetInputSerializer, \
    AccidentSerializer



@csrf_exempt
def info_street(request):
    if request.method=="GET":
        return HttpResponse(json.dumps(SectionSerializer(Section.objects.all(),many=True).data))

@csrf_exempt
def street(request):
    try:
        if request.method=="POST":
            #Todo serializable is_valid
            #Todo check all parameters check if we need to send before-hand
            #todo check if there isnt any overlap
            #Todo when creating a section need to verify the connections
            '''
            Creating a new street
            '''
            data=json.loads(request.body)
            name=data.get("name")
            begin_coord_x,begin_coord_y=(data.get("beginning_coords")[0],data.get("beginning_coords")[1])
            ending_coord_x,ending_coord_y=(data.get("ending_coords")[0],data.get("ending_coords")[1])
            length=math.hypot(begin_coord_x-ending_coord_x,begin_coord_y-ending_coord_y)

            street_obj=Street(name=name,
                          begin_coord_x=begin_coord_x,
                          begin_coord_y=begin_coord_y,
                          ending_coord_x=ending_coord_x,
                          ending_coord_y=ending_coord_y,
                          length=length)
            street_obj.save()
            '''
            Turning the street into different sections
            Each section is aprox 500m of a street, if the street is made of sections that aren't divisible by 500
            the last section will be the rest 1200=500+500+200
            '''
            number_of_divisions=(length/(500))
            stop=False
            for i in range(0,math.ceil(number_of_divisions)+1):

                begin_x=begin_coord_x+(i*((ending_coord_x-begin_coord_x)/number_of_divisions))
                begin_y=begin_coord_y+(i*((ending_coord_y-begin_coord_y)/number_of_divisions))
                end_coord_x=begin_coord_x+((i+1)*((ending_coord_x-begin_coord_x)/number_of_divisions))
                end_coord_y=begin_coord_y+((i+1)*((ending_coord_y-begin_coord_y)/number_of_divisions))

                if i==0:
                    begin_x=begin_coord_x
                    begin_y=begin_coord_y
                if end_coord_x>ending_coord_x:
                    end_coord_x=ending_coord_x
                    stop=True
                if end_coord_y>ending_coord_y:
                    end_coord_y=ending_coord_y
                    stop=True
                if begin_x==end_coord_x and begin_y==end_coord_y:
                    break
                create_section(street_obj,begin_x,begin_y,end_coord_x,end_coord_y,True)
                create_section(street_obj,begin_x,begin_y,end_coord_x,end_coord_y,False)
                if stop:
                    break
            return HttpResponse(json.dumps(StreetInputSerializer(street_obj).data))
    except Exception as e:
        #TODO make this according to standards
        print(e)
        return HttpResponse("ERROR")

@csrf_exempt
def car_to_street(request):
    try:
        if request.method=="PUT":
            section=Section.objects.get(id=json.loads(request.body).get('id'))
            section.number_cars += 1
            section.save()
            add_to_transit(section)
            return HttpResponse(json.dumps(SectionSerializer(section).data))
        elif request.method=="DELETE":
            section = Section.objects.get(id=json.loads(request.body).get('id'))
            section.number_cars -= 1
            section.save()
            return HttpResponse(json.dumps(SectionSerializer(section).data))
    except Exception as e:
        print(e)
        return HttpResponse("ERROR")

@csrf_exempt
def add_to_accident(request):
    if request.method=="POST":
        data=json.loads(request.body)
        section=Section.objects.get(id=data.get("id"))
        accident= Accident(section=section,coord_x=data.get("x_coord"),coord_y=data.get("y_coord"),date=datetime.now(timezone.utc))
        accident.save()
        return HttpResponse(json.dumps(AccidentSerializer(accident).data))
    return

def add_to_transit(section,transit=200):
    time_of_transit = datetime.now(timezone.utc)
    last_time_of_transit = sorted(Transit.objects.filter(section=section),key=lambda transit:transit.date,reverse=True)
    if section.number_cars>transit:
        if last_time_of_transit==[]:
            transit = Transit(date=time_of_transit, section=section)
            transit.save()
        if last_time_of_transit[0].date+timedelta(minutes=30)<time_of_transit:
            transit = Transit(date=time_of_transit,section=section)
            transit.save()

def create_section(street,coord_x,coord_y,end_x,end_y,direction):
    section = Section(street=street,
                      beginning_coords_x=coord_x,
                      beginning_coords_y=coord_y,
                      ending_coords_x=end_x,
                      ending_coords_y=end_y,
                      actual_direction=direction)
    section.save()
