from django.contrib import admin
from .models import Client, Category, Dish, Flavor, Restaurant, Shedule, Day, Social, Media

# Register your models here.
admin.site.register(Client)
admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(Flavor)
admin.site.register(Restaurant)
admin.site.register(Day)
admin.site.register(Shedule)
admin.site.register(Social)
admin.site.register(Media)