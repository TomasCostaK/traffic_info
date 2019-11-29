from django.db import models
from rest_framework import serializers


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
    def type(self,Section):
        if Section.n_accident>0:
            return 'Congested'
        if 100<Section.number_cars<200:
            return 'Medium'
        if Section.number_cars>200:
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
                'transit_type')
''' End of Serializables for Road Map'''

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
        fields=('coord_x',
                'coord_y',
                'date',
                'section')