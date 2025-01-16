from django.contrib import admin
from .models import Pizza
from .models import Order

admin.site.register(Pizza)
admin.site.register(Order)