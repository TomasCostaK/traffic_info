from django.http import HttpResponse
from django.shortcuts import render
import pika
import json
import math
from datetime import datetime,timezone,timedelta
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import responses
from rest_framework import status

from TrafficJammer.models import Street, \
    Section, \
    Transit, \
    Accident, \
    Car, \
    Blocked, \
    SectionSerializer, \
    StreetSerializer, \
    StreetInputSerializer, \
    SectionStatisticsSerializer, \
    CarSerializer, \
    AccidentSerializer



@csrf_exempt
def info_street(request):
    if request.method=="GET":
        return HttpResponse(json.dumps(SectionSerializer(Section.objects.all(),many=True).data),status=status.HTTP_200_OK)

@csrf_exempt
def street(request):
    try:
        if request.method=="POST":
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
            return HttpResponse(json.dumps(StreetInputSerializer(street_obj).data),status=status.HTTP_200_OK)
    except:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def car_to_street(request):
    try:
        if request.method=="PUT":
            data=json.loads(request.body)
            section=Section.objects.get(id=data.get('id'))
            section.number_cars += 1
            section.save()
            add_to_transit(section)
            car=Car(license_plate=data.get('plate'),section=section)
            car.save()
            return HttpResponse(json.dumps(SectionSerializer(section).data)+json.dumps(CarSerializer(car).data),status=status.HTTP_200_OK)
        elif request.method=="DELETE":
            data=json.loads(request.body)
            car=Car.objects.get(license_plate=data.get('plate'))
            section=Section.objects.get(id=car.section.id)
            section.number_cars-=1
            car.delete()
            section.save()
            return HttpResponse(json.dumps(SectionSerializer(section).data),status=status.HTTP_200_OK)
        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
    except Car.DoesNotExist:
        return HttpResponse("Car not found",status=status.HTTP_404_NOT_FOUND)
    except Section.DoesNotExist:
        return HttpResponse("Section not found",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def add_to_accident(request):
    try:
        if request.method=="POST":
            data=json.loads(request.body)
            section=Section.objects.get(id=data.get("id"))
            accident= Accident(section=section,coord_x=data.get("x_coord"),coord_y=data.get("y_coord"),date=datetime.now(timezone.utc))
            accident.save()
            return HttpResponse(json.dumps(AccidentSerializer(accident).data),status=status.HTTP_200_OK)
        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
    except Section.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

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


def get_car(request):
    try:
        if request.method=='GET':
            data=json.loads(request.body)
            car=Car.objects.get(license_plate=data.get('license_plate'))
            return HttpResponse(json.dumps(CarSerializer(car).data),status=status.HTTP_200_OK)
        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
    except Car.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

def all_cars(request):
    try:
        if request.method=="GET":
            data=json.loads(request.body)
            section=Section.objects.get(id=data.get('id'))
            car=Car.objects.filter(section=section)
            return HttpResponse(json.dumps(CarSerializer(car,many=True).data),status=status.HTTP_200_OK)
        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
    except Section.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

def statistics(request):
    day_to_int={"Monday":2,"Tuesday":3,"Wednesday":4,"Thursday":5,"Friday":6,"Saturday":7,"Sunday":1}
    try:
        if request.method=="GET":
            data=json.loads(request.body)
            print(data)
            begin_time=data.get("begin").split("-")
            begin_time=datetime(int(begin_time[0]), int(begin_time[1]), int(begin_time[2]), 0, 0, 0, 0, timezone.utc)
            end_time=data.get("end").split("-")
            end_time=datetime(int(end_time[0]),int(end_time[1]),int(end_time[2]),0,0,0,0,timezone.utc)
            id=data.get("id")
            section=Section.objects.get(id=id)
            blocked=Blocked.objects.filter(begin__range=(begin_time,end_time),end__range=(begin_time,end_time))
            if "week_day" in data:
                transit = Transit.objects.filter(date__range=(begin_time, end_time),date__week_day=day_to_int.get(data.get("week_day")))
                accident = Accident.objects.filter(date__range=(begin_time, end_time),date__week_day=day_to_int.get(data.get("week_day")))
            else:
                transit=Transit.objects.filter(date__range=(begin_time,end_time))
                accident=Accident.objects.filter(date__range=(begin_time,end_time))
            return HttpResponse(json.dumps(SectionStatisticsSerializer(section,
                                                                       context={"transit":transit,"blocked":blocked,"accident":accident}).data)
                                ,status=status.HTTP_200_OK)
        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
    except Section.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def visibility(request):
    if request.method=="POST":
        try:
            data=json.loads(request.body)
            section=Section.objects.get(id=data.get("id"))
            section.visibility=data.get("visibility")
            section.save()
            return HttpResponse(json.dumps(SectionSerializer(section).data),status=status.HTTP_200_OK)
        except Section.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    else:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def police(request):
    if request.method=="PUT":
        try:
            data= json.loads(request.body)
            section=Section.objects.get(id=data.get)
            section.police=data.get("police")
            section.save()
            return HttpResponse(json.dumps(SectionSerializer(section).data),status=status.HTTP_200_OK)
        except Section.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    else:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

#Todo see if time should come from sensor
@csrf_exempt
def roadblock(request):
    try:
        if request.method=="PUT":
            data = json.loads(request.body)
            section = Section.objects.get(id=data.get("id"))
            section.roadblock=True
            section.save()
            if len(Blocked.objects.filter(section=section,end__isnull=True)):
                return HttpResponse("A road can only be blocked once",status=status.HTTP_304_NOT_MODIFIED)
            road_block=Blocked(section=section,begin=datetime.now(timezone.utc))
            road_block.save()
            return HttpResponse("Road Blocked",status=status.HTTP_200_OK)
        elif request.method=="DELETE":
            data = json.loads(request.body)
            road_block=Blocked.objects.get(section=data.get("id"),end__isnull=True)
            road_block.end=datetime.now(timezone.utc)
            road_block.save()
            return HttpResponse("Road unblocked",status=status.HTTP_200_OK)
        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
    except Section.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    except Blocked.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)