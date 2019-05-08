from django.contrib import admin
from .models import Client, Category, Dish, Flavor, Restaurant, Shedule

# Register your models here.
admin.site.register(Client)
admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(Flavor)
admin.site.register(Restaurant)
admin.site.register(Shedule)