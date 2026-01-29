from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from .models import DataModels
import json
from django.views.decorators.csrf import csrf_exempt



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
def showData(request,id):
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
        data=DataModels.objects.get(id=id)
        return JsonResponse({
            "id": data.id,
            "name": data.name,
            "age": data.age,
            "salary": data.salary
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


# Create your views here.
