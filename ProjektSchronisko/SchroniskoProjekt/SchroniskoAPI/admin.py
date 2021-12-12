from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Zwierze)
admin.site.register(Pracownik)
admin.site.register(Zabieg)
admin.site.register(Adopcja)
admin.site.register(Stanowisko)
admin.site.register(RodzajeZabiegow)

