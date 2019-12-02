from django.db import models
from rest_framework import serializers

'''Start of models'''
class Street(models.Model):
    name=models.CharField(max_length=80)
    begin_coord_x=models.IntegerField()
    begin_coord_y=models.IntegerField()
    ending_coord_x=models.IntegerField()
    ending_coord_y=models.IntegerField()
    length=models.IntegerField()


class Section(models.Model):
    number_cars=models.IntegerField(default=0)
    # True means left-to-right
    # False means right-to-left
    actual_direction=models.BooleanField()
    # Number of accidents at the moment
    n_accident=models.IntegerField(default=0)
    beginning_coords_x=models.IntegerField()
    ending_coords_x=models.IntegerField()
    beginning_coords_y=models.IntegerField()
    ending_coords_y=models.IntegerField()
    street=models.ForeignKey(Street,on_delete=models.CASCADE)
    connect_to=models.ManyToManyField("self",blank=True)
    visibility=models.IntegerField(default=100)
    roadblock=models.BooleanField(default=False)
    police=models.BooleanField(default=True)
    class Meta:
        unique_together=(('street','beginning_coords_x','beginning_coords_y','actual_direction'),)

class Accident(models.Model):
    coord_x=models.IntegerField()
    coord_y=models.IntegerField()
    section=models.ForeignKey(Section,on_delete=models.CASCADE)
    date=models.DateTimeField()

class Transit(models.Model):
    date=models.DateTimeField()
    section=models.ForeignKey(Section,on_delete=models.CASCADE)

class Blocked(models.Model):
    section=models.ForeignKey(Section,on_delete=models.CASCADE)
    begin=models.DateTimeField()
    end=models.DateTimeField(blank=True,null=True)

class Car(models.Model):
    license_plate=models.CharField(max_length=6,primary_key=True)
    section=models.ForeignKey(Section,on_delete=models.CASCADE)

'''End of models'''

'''Serializables for input'''
class StreetInputSerializer(serializers.ModelSerializer):
    class Meta:
        model=Street
        fields = ('name',
                  'begin_coord_x',
                  'begin_coord_y',
                  'ending_coord_x',
                  'ending_coord_y',
                  'length',
                  )
'''End of serializables for input'''

''' Serializables to send data for roadmap '''
class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Street
        fields = ('name','id',)

class SectionSerializer(serializers.ModelSerializer):
    street=StreetSerializer()
    transit_type=serializers.SerializerMethodField('type')
    def type(self,Section,transit_limit=100):
        if Section.visibility<50:
            transit_limit=50

        if Section.roadblock:
            return 'Blocked'
        elif Section.n_accident>0:
            return 'Congested'
        elif transit_limit<Section.number_cars<2*transit_limit:
            return 'Medium'
        elif Section.number_cars>2*transit_limit:
            return 'Congested'
        else:
            return 'Normal'

    class Meta:
        model = Section
        fields=('id',
                'number_cars',
                'actual_direction',
                'n_accident',
                'beginning_coords_x',
                'beginning_coords_y',
                'ending_coords_x',
                'ending_coords_y',
                'street',
                'transit_type',
                'police')

''' End of Serializables for Road Map'''

'''Serializables for Accident and Cars'''
class SmallSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Section
        fields=('id')
        exclude=['number_cars',
                 'actual_direction',
                 'n_accident',
                 'beginning_coords_x',
                 'beginning_coords_y',
                 'street']

class AccidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accident
        fields = ('coord_x',
                'coord_y',
                'date',
                'section')

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Car
        fields=('license_plate',
                'section')
''' End Serializables for Accident and Car'''


'''Serializable for Roadblock'''
'''End of Serializable for Roadblock'''