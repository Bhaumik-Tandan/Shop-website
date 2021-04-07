from django.db.models import *


class User(Model):
    name = CharField(max_length=50)
    email = CharField(max_length=50)
    phone = CharField(max_length=50)
    address = CharField(max_length=200)
    password = CharField(max_length=50)
    i = AutoField

    def __str__(self):
        return self.name


class Product(Model):
    name = CharField(max_length=50, default="", unique="true")
    description = CharField(max_length=200, default="")
    available = CharField(max_length=5, default="", choices=[
                          ("y", "Yes"), ("n", "No")])
    price = FloatField(default=1000.00)
    category = CharField(max_length=50, default="", choices=[
        ("Cakes", "Cakes"), ("Snacks", "Snacks"), ("Sweets", "Sweets")])
    recomended = CharField(max_length=5, default="", choices=[
                          ("y", "Yes"), ("n", "No")])
    image = ImageField(default=None)

    def __str__(self):
        return self.name
