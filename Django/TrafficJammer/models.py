from django.db import models

class Street(models.Model):
    name=models.CharField(max_length=80)
    begin_coord_x=models.IntegerField()
    begin_coord_y=models.IntegerField()
    ending_coord_x=models.IntegerField()
    ending_coord_y=models.IntegerField()
    length=models.IntegerField()
    connect_to=models.ManyToManyField("self",blank=True)

class Section(models.Model):
    number_cars=models.IntegerField()
    # True means left-to-right
    # False means right-to-left
    actual_direction=models.BooleanField()
    # Number of accidents at the moment
    accident=models.IntegerField()
    beggining_coords_x=models.IntegerField()
    beggining_coords_y=models.IntegerField()
    street=models.ForeignKey(Street,on_delete=models.CASCADE)

    class Meta:
        unique_together=(('street','beggining_coords_x','beggining_coords_y','actual_direction'),)

class Acidente(models.Model):
    coord_x=models.IntegerField()
    coord_y=models.IntegerField()
    section=models.ForeignKey(Section,on_delete=models.CASCADE)
    date=models.DateField()

class Transit(models.Model):
    date=models.DateField()
    section=models.ForeignKey(Section)