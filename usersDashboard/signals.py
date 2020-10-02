from django.db.models.signals import post_save  
from django.dispatch import receiver
from profiles.models import Donor,RegularUser,Grievance
from .models import Notification

@receiver(post_save, sender=Donor)
def notification_handler(sender,created,instance,*args, **kwargs):
    if instance:
        pass