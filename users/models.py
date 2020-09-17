from django.db import models
from django.contrib.auth.models import AbstractUser 

Gender = (
    ('Male', 'Male'),
    ('Female', 'Female') 
)

UserType = (
    ('Donor / organization', 'Donor / organization'),
    ('Regular user','Regular user'),

)
class User(AbstractUser):
    profile_picture = models.ImageField(default='profile_pictures/default.png' , upload_to='profilepictures')
    phone_number = models.IntegerField( blank=True, null=True)
    userType = models.CharField(choices=UserType, max_length=50, blank=True,null=True)
    gender = models.CharField(choices=Gender, max_length=50)
 
    



    def __str__(self):
        return self.username
