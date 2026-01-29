from django.urls import path
from . import views


urlpatterns = [
    path("data/",views.basicData),
    path("showData/<int:id>",views.showData),
    path("showDataHtml/",views.sendingData)

]
