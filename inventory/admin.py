from django.contrib import admin
from .models import Almacen, ControlInventario, DetalleControl, Item, RecuentoDetalle

admin.site.register(Almacen)
admin.site.register(ControlInventario)
admin.site.register(DetalleControl)
admin.site.register(Item)
admin.site.register(RecuentoDetalle)
