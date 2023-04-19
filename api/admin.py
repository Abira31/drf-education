from django.contrib import admin

from .models import *
# Register your models here.
model = [Subject,Groups,Teachers,Students,Subjects,Marks]
for m in model:
    admin.site.register(m)

