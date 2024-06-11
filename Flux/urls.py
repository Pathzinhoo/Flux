from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from devices.views import CollectedDataViewset
from rest_framework import routers
from . import mqtt

router = routers.DefaultRouter()
router.register(r'data',CollectedDataViewset)

def home(request):
    context = {
        "pageTitle":"Plantios"
    }
    return render(request, 'planting.html',context=context)

urlpatterns = [
    path('', home, name='home' ),
    path('api/', include(router.urls)),
    path('planting/', include('plants.urls')),
    path('admin/', admin.site.urls),
]

mqtt.client.loop_start()