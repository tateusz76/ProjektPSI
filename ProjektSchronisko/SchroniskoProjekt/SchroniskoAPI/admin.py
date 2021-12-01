from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Zwierze)
admin.site.register(Pracownik)
admin.site.register(Zabieg)
admin.site.register(Magazyn)
admin.site.register(Zamowienia)
admin.site.register(Datki)

