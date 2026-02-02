from django.urls import path
from . import views


urlpatterns = [
    path("data/",views.basicData),
    path("showData/",views.showData),
    path("showDataHtml/",views.sendingData),
    path("allData/",views.allData),
    path("api/user/",views.getingUserData),
]
