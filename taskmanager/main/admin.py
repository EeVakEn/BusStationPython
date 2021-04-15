from django.contrib import admin
from .models import Bus, Route, Flight
from django.contrib.auth.models import User


admin.site.register(Bus)
admin.site.register(Route)
admin.site.register(Flight)