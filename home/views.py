from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from .models import DataModels
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator




# data1={
#     "name":"akash",
#     "age":23,
#     "salary":3434343
# }

def basicData(request):
    return render(request,"data.html")

# def userData(request):
#     return JsonResponse(data1)
    

# @csrf_exempt
def showData(request):
    if request.method == "POST":
        data = {
            "name": request.POST.get("name"),
            "age": request.POST.get("age"),
            "salary": request.POST.get("salary")
        }
        # save data to model from frontend 
        name=request.POST.get("name"),
        age=request.POST.get("age"),
        salary=request.POST.get("salary")
        DataModels.objects.create(
            name=name,
            age=age,
            salary=salary
        )
        return JsonResponse(data)
    if request.method=="GET":
        data = list(DataModels.objects.all().values())
        return JsonResponse({
            "data":data
        })

    return JsonResponse(
        {"error": "Only POST method allowed"},
        status=405
    )

def sendingData(request):
    context = {}
    if request.method=="POST":
        name=request.POST.get("name")
        age=request.POST.get("age")
        salary=request.POST.get("salary")
        context = {
        'name': name,
        'age':age,
        "salary":salary
    }
    return render(request,"renderData.html",context)

data1={
    "name":"aman",
    "age":20
}
def getingUserData(request):
    return JsonResponse({
        "data":data1
    })

def allData(request):
    data=list(DataModels.objects.all().values())
    print(data)
    context={
        "data":data
    }
    print(context)
    return render(request,"allData.html",context)

# Create your views here.
