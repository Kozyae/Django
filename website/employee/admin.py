from django.contrib import admin
from .models import Employee, Sick, Annual, Unpay

admin.site.register(Employee)
admin.site.register(Sick)
admin.site.register(Annual)
admin.site.register(Unpay)

