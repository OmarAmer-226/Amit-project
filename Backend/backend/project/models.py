from django.db import models
from django.contrib.auth.models import User


class Products(models.Model):
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    description = models.TextField(blank = True)
    image = models.ImageField(null=True , blank=True , default="/placeholder.png")

    def __str__(self):
        return self.name


class Breakfast(models.Model):
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    description = models.TextField(blank = True)
    image = models.ImageField(null=True , blank=True , default="/placeholder.png")

    def __str__(self):
        return self.name


class MainDishes(models.Model):
    name = models.CharField( max_length = 100)
    price = models.DecimalField( max_digits = 10, decimal_places = 3)
    description = models.TextField(blank = True)
    image = models.ImageField( null= True , blank= True , default="/placeholder.png")

    def __str__(self):
        return self.name
    
class Drinks(models.Model):
    name = models.CharField( max_length = 100)
    price = models.DecimalField( max_digits = 10, decimal_places = 2)
    description = models.TextField (blank = True)
    image = models.ImageField( null = True , blank = True, default='/path/to/default/image.png' )

    def __str__(self):
        return self.name


class Dessert(models.Model):
    name = models.CharField( max_length = 100)
    price = models.DecimalField( max_digits = 10, decimal_places = 2)
    description = models.TextField (blank = True)
    image = models.ImageField( null = True , blank = True, default='/path/to/default/image.png' )

    def __str__(self):
        return self.name


class Table(models.Model):
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f"Table {self.number} (Capacity: {self.capacity})"





class TableBooking(models.Model):
    username = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)  # Store phone as string to accommodate various formats
    date = models.DateField()
    time = models.TimeField()
    total = models.PositiveIntegerField()  # Assuming total is the number of people
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.date} {self.time}"
    



