from django.contrib import admin
from .models import Producto, Auto, Evento, Sucursal, Comentario

# Register your models here.
admin.site.register(Producto)
admin.site.register(Auto)
admin.site.register(Evento)
admin.site.register(Sucursal)
admin.site.register(Comentario)
