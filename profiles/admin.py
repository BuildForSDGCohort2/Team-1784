from django.contrib import admin
from . import models

admin.site.register(models.RegularUser)
admin.site.register(models.Donor)
admin.site.register(models.Grievance)
admin.site.register(models.Starred)

