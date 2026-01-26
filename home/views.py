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
    

@csrf_exempt
def showData(request):
    if request.method == "POST":
        data = {
            "name": request.POST.get("name"),
            "age": request.POST.get("age"),
            "salary": request.POST.get("salary")
        }
        return JsonResponse(data)
    if request.method=="GET":
        data=DataModels.objects.all()
        return JsonResponse(data, safe=False)
    return JsonResponse(
        {"error": "Only POST method allowed"},
        status=405
    )



# Create your views here.
