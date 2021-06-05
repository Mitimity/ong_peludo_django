from django.contrib import admin
#importar modelos
from .models import Especie,Mascota

# Register your models here.
admin.site.register(Especie)
admin.site.register(Mascota)