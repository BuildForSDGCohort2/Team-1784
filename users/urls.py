from django.urls import path
from .views import signupView,logoutView,loginView
# from django.contrib.auth import views as auth_views


app_name = 'users'

urlpatterns = [
    path('login/', loginView, name='login'),
    path('signup/', signupView , name='signup'),
    path('logout/', logoutView, name='logout'),
    
]

