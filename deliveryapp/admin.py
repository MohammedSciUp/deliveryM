from django.contrib import admin
from .models import Deliverer, Order

# Register your models here.
admin.site.register(Deliverer)
admin.site.register(Order)