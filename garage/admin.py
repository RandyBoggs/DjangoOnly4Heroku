from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin, register
from garage.models import VehicleType, Point, PointType 

@register(VehicleType)
class VehicleTypeAdmin(ModelAdmin):
    list_display = ('name',)

@register(Point)
class PointAdmin(ModelAdmin):
    list_display = ('name', 'longitude', 'latitude')

@register(PointType)
class PointTypeAdmin(ModelAdmin):
    list_display = ('name',)

# from material.admin.sites import site
from django.contrib.auth.models import User, Group 

admin.site.unregister(User)
admin.site.unregister(Group)
