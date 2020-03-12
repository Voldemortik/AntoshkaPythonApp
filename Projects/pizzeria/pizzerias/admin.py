from django.contrib import admin

# Register your models here.
from pizzerias.models import Pizza,Toppings
admin.site.register(Pizza)
admin.site.register(Toppings)