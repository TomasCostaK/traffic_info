from django.contrib import admin
from TrafficJammer.models import Street,Section,Transit,Accident
# Register your models here.
admin.site.register(Street)
admin.site.register(Section)
admin.site.register(Transit)
admin.site.register(Accident)