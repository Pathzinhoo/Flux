from django.shortcuts import render
from devices.models import CollectedData
import json


# Create your views here.
def plantingResum(request):
    
    lat = CollectedData.objects.all().last()
    data = json.loads(lat.data)
    print(data["temp"])
    context = {
        "pageTitle":"Resumo",
        "temp": int(data["temp"])
    }
    return render(request, 'plantingResum.html', context=context)