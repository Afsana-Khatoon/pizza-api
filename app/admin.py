from django.contrib import admin
from .models import *


admin.site.register(PizzaType)
admin.site.register(SizeType)
admin.site.register(ToppingType)
admin.site.register(Pizza)