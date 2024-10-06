# inventory/views.py
from .models import ControlInventario, RecuentoDetalle
from .serializers import ControlInventarioSerializer, RecuentoDetalleSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import filters

# Create your views here.

class OptionalPagination(PageNumberPagination):
    
    def paginate_queryset(self, queryset, request, view=None):
        page = request.query_params.get('page') 
        if page:
            return super().paginate_queryset(queryset, request, view=view)
        return None

class ControlInventarioListCreateView(generics.ListCreateAPIView):
    queryset = ControlInventario.objects.all()
    serializer_class = ControlInventarioSerializer
    pagination_class = OptionalPagination
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # filterset_fields = ['cedula']
    # search_fields = ['^cedula', 'nombre', 'apellido']
    
class ControlInventarioDetailView(generics.RetrieveUpdateAPIView): 
    # permission_classes = (IsAuthenticated,)
    queryset = ControlInventario.objects.all()
    serializer_class = ControlInventarioSerializer
    
class RecuentoDetalleListCreateView(generics.ListCreateAPIView):
    queryset = RecuentoDetalle.objects.all()
    serializer_class = RecuentoDetalleSerializer
    pagination_class = OptionalPagination
    