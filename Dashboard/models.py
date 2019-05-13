from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Timestamp model to save the date of every transaction of the rest of the models
class Timestamp(models.Model):
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    delete_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


# Client model that will be used to register new clients in the system
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15,null=True, blank=True)
    plan = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username




# Restaurant model to every restaurant saved in the system.
class Restaurant(Timestamp):
    name = models.CharField(max_length=50)
    address = models.TextField()
    logo_url = models.URLField(max_length=200)
    web_site = models.URLField(max_length=200)
    status = models.BooleanField('open', blank=False, null=False, default=True)
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    categories = models.ManyToManyField('Category')
    flavors = models.ManyToManyField('Flavor')

    def __str__(self):
        return self.name


class Category(Timestamp):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Flavor(Timestamp):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Shedule(models.Model):
    days = models.TextField()
    time_open = models.DateTimeField()
    time_close = models.DateTimeField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.restaurant.name
