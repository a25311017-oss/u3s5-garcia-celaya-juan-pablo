# admin: el módulo del panel /admin
from django.contrib import admin
# Servicio: el modelo de esta misma app
from .models import Servicio

# register: registro simple, sin personalizar nada
admin.site.register(Servicio)