from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def basicData(request):
    return render(request,"data.html")

# Create your views here.
