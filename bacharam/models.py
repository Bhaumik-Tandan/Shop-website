from django.db import models
from django.db.models import *


class Products(models.Model):
    pid = AutoField
    img = ImageField(upload_to='static/products')
    desc = CharField()
    pr = FloatField()
    dis = FloatField()
