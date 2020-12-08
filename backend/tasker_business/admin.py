from django.contrib import admin
from .models import BusinessPhoto, TaskerAvailability, TaskerSkill, Timeslot

admin.site.register(TaskerAvailability)
admin.site.register(BusinessPhoto)
admin.site.register(Timeslot)
admin.site.register(TaskerSkill)

# Register your models here.
