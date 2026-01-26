from django.urls import path
from . import views


urlpatterns = [
    path("data/",views.basicData),
    path("showData/",views.showData),

]
