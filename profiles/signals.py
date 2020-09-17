from django.db.models.signals import post_save  
from django.dispatch import receiver
from users.models import User
from .models import RegularUser,Grievance,Donor,Starred




@receiver(post_save, sender=User)
def profile(sender,created,instance,*args, **kwargs):
    if created:
        if instance.userType == 'Regular user':
            RegularUser.objects.create(user=instance) 
        else:
            Donor.objects.create(user=instance)


@receiver(post_save, sender=RegularUser)
def grievance_handler(sender,created,instance,*args, **kwargs):
    if created:
        Grievance.objects.create(regular_user=instance) 
     
                
 
        
            
                
     
