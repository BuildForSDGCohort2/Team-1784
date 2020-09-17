from django.urls import path
from . import views

app_name = 'discover'

urlpatterns = [
    path('', views.discoverView, name='index'),
 
]

