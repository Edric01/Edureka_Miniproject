from django.shortcuts import render
from . import models
from rest_framework.decorators import api_view
from .serializers import ServiceSerializer
from rest_framework.response import Response

global cart_box
cart_box=[]
# Create your views here.
def home(request):
    return render(request,"base.html")
def contact(request):
    if request.method=="POST":
        name=request.POST.get("inputName")
        email=request.POST.get("inputEmail")
        message1=request.POST.get("inputMessage")
        # print(request.POST)
        # print(name)
        if name !=None or name!="":
            message=models.Messsage(Name=name,Email=email,MessageText=message1)

            message.save()
        
            print("Created User")
            print(contact)
    return render(request,"contacts.html")


@api_view(['GET'])
def getServices(request):
    # person={"Name":"Edric","Age":23}
    services=models.Service.objects.all()
    serviceSerializer=ServiceSerializer(services,many=True)
    # print(serviceSerializer.data)
    # for serv in serviceSerializer.data:
    #     print(serv["Name"])
    # return Response(serviceSerializer.data)
    return render(request,"service.html",{"data":serviceSerializer.data})

@api_view(['POST'])
def cart(request,service):
    if request.method=="POST":    
        services=models.Service.objects.all()
        serviceSerializer=ServiceSerializer(services,many=True)
        for serv in serviceSerializer.data:
            if serv["Name"]==service:
                globals()['cart_box'].append(serv)
    return render(request,"service.html",{"data":serviceSerializer.data})

def checkout(request):
    if globals()['cart_box']==[]:
        services=models.Service.objects.all()
        serviceSerializer=ServiceSerializer(services,many=True)
        return render(request,"service.html",{"data":serviceSerializer.data})
    else:
        bought=[]
        total=0
        for s in globals()['cart_box']:
            print(s)
            total+=s["price"]
            bought.append(s)
        globals()['cart_box']=[]
        return render(request,"cart.html",{"Total":total,'cart':bought})
    