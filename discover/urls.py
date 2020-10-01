from django.urls import path
from . import views

app_name = 'discover'

urlpatterns = [
    path('', views.discoverView, name='index'),
    path('<int:id>/detail', views.discoverDetail, name='detail'),
    path('add-regular-user/<int:id>/add', views.addReqularUser, name='add'),
    path('regular-user/<int:id>/remove', views.removeReqularUser, name='remove'),
    path('regular-user/<int:id>/remove-1', views.removeRegUser, name='remove1'),
 
]

