from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import *
from APIChapter2.models import *
# Create your views here.
def register(request):
    if request.method=="POST":
        Name=request.POST['Name']
        Address=request.POST['Address']
        City=request.POST['City'] 
        State=request.POST['State'] 
        Mobile=request.POST['Mobile']
        EmailId =request.POST['EmailId']
        Password=request.POST['Password']
        reg=Customer(Name=Name,Address=Address,City=City,State=State,Mobile=Mobile,EmailId=EmailId,Password=Password)
        reg.save()
    return render(request,"register.html")


def login(request):
    if request.method=="POST":
        EmailId =request.POST.get('Emaild')
        Password=request.POST.get('Password')
        user=Customer.objects.filter(EmailId=EmailId,Password=Password)
        print(EmailId)
        print(Password)

        if user.exists():
            return HttpResponse(user.first().Name)

        else:
            return HttpResponse("Khatam Tata Bye Bye")    

        

    return render(request,"login.html")


@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def taskList(request):
	tasks = Customer.objects.all().order_by('id')
	serializers = API(tasks, many=True)
	return Response(serializers.data)

@api_view(['GET'])
def taskDetail(request, pk):
	tasks = Customer.objects.get(id=pk)
	serializers = API(tasks, many=False)
	return Response(serializers.data)


@api_view(['POST'])
def taskCreate(request):
	serializer = API(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
	task = Customer.objects.get(id=pk)
	serializer = API(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Customer.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')