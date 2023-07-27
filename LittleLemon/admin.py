from django.contrib import admin

# Register your models here.
from LittleLemon.models import *



admin.site.register(Order)
admin.site.register(MenuItem)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(OrderItem)