from django.http import HttpResponse
from django.shortcuts import render
import json
import urllib.request
from service.models import Service
  

def aboutus(request):
    return HttpResponse("working")


def homepage(request):
    servicesData=Service.objects.all()
    for a in servicesData:
        print("here is our data");
        print(servicesData);
    
    if request.method == 'GET':
         source = urllib.request.urlopen(
            'https://api.countapi.xyz/hit/namespace/key').read()
         data = json.loads(source)
    
    
    
    data={
        'val':str(data['value']),
        'title':'home page hehe',
        'list':['item1','item2','item3']
        
    }
    return render(request,"index.html",data)