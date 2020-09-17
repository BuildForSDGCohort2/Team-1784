from django.db import models
from users.models import User

class RegularUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='regular_user')
    brief_introduction = models.TextField(blank=True, null=True)
    age  = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=100)
    region_or_state = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    interest = models.CharField(max_length=1000, blank=True, null=True)
    education_level = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username

Type_choice = (
    ('Individual','Individual'),
    ('Organization', 'Organization')
)
class Donor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='donor')
    i_am = models.CharField(max_length=30, choices=Type_choice,null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.username





class Grievance(models.Model):
    regular_user = models.ForeignKey(RegularUser, on_delete=models.CASCADE, blank=True, null=True)
    talent = models.CharField(max_length=500, blank=True, null=True)
    help_you_need = models.CharField(max_length=2000, blank=True, null=True)
    demo_in_text = models.TextField(blank=True, null=True)
    demo = models.FileField(upload_to='demo', blank=True, null=True)

    def __str__(self):
        return self.regular_user.user.username

class Starred(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE, blank=True, null=True)
    starred = models.ManyToManyField(Grievance, related_name='starred')

