from django.db import models
from django.forms import ImageField

class Model3Ds(models.Model):
    id = models.BigAutoField('3d id', primary_key=True)
    data = models.JSONField('3d model data')

    class Meta:
        db_table = 'model3ds'


class HomeBages(models.Model):
    id = models.BigAutoField('home bage id', primary_key=True)
    model_3d = models.OneToOneField(Model3Ds,on_delete=models.SET_NULL, null=True)
    logo = models.ImageField()

    class Meta:
        db_table = 'homebages'