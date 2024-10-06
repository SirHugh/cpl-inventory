from rest_framework import serializers
from .models import Item, Almacen, ControlInventario, DetalleControl, RecuentoDetalle

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        
class AlmacenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Almacen
        fields = '__all__'


class ControlInventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlInventario
        fields = '__all__'

class DetalleControlSerializar(serializers.ModelSerializer):
    class Meta:
        model = DetalleControl
        fields = '__all__'

class RecuentoDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecuentoDetalle
        fields = '__all__'

