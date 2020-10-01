from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('donor/', views.donorDashboard, name='duser'),

]

