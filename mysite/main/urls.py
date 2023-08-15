from django.urls import path

from . import views 

urlpatterns = {
path("", views.index, name="index"),
# "" string the path where we've given | views.index and it will go to appropriate view from the views file or views.py 
}