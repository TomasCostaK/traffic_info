"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from TrafficJammer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info_street/',views.info_street,name="info"),
    path('street/',views.street,name="crud_street"),
    path('car/',views.car_to_street,name="crud_car"),
    path('accident/',views.add_to_accident,name="accident")
]
