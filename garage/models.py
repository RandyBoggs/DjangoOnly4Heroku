from django.db import models

# Create your models here.
class VehicleType (models.Model):
    name = models.CharField(max_length=100)

    class Meta:
            verbose_name = 'Тип АТС'
            verbose_name_plural = 'Типы АТС'

class PointType (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
            return self.name
 
    class Meta:
            verbose_name = 'Тип точки'
            verbose_name_plural = 'Типы точек'
 

class Point (models.Model):
    name = models.CharField(max_length=100)
    longitude = models.CharField(max_length=10)
    latitude = models.CharField(max_length=10)
    point_type = models.ForeignKey(PointType, on_delete=models.CASCADE, null=True)

    class Meta:
            constraints = [
                models.CheckConstraint(check=models.Q(age__gte=18), name='age_gte_18'),
            ]
            verbose_name = 'Точка'
            verbose_name_plural = 'Точки'
            