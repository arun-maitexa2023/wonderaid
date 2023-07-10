from django.contrib import admin
from .models import log, user, Hotel,Restaurent,Resort,Travels,Guide

# Register your models here.
admin.site.register(log)
admin.site.register(user)
admin.site.register(Hotel)
admin.site.register(Restaurent)
admin.site.register(Resort)
admin.site.register(Travels)
admin.site.register(Guide)
