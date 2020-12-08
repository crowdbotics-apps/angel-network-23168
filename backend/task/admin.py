from django.contrib import admin
from .models import Message, Rating, Task, TaskTransaction

admin.site.register(Rating)
admin.site.register(Task)
admin.site.register(TaskTransaction)
admin.site.register(Message)

# Register your models here.
