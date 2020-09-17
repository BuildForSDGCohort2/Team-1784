from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('regular-user/', views.regularUser, name='reguser'),
    path('donor-user/', views.donorUser, name='duser'),
    path('grievance/', views.grievanceView, name='guser'),
    path('user/', views.userProfile, name='profile'),
]

