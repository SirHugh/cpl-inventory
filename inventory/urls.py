from django.urls import path
from rest_framework.documentation import include_docs_urls 
from .views import ControlInventarioDetailView, ControlInventarioListCreateView, RecuentoDetalleListCreateView 

urlpatterns = [ 
    path("docs/", include_docs_urls(title="Auth API")), 
    path('control-inventario/', ControlInventarioListCreateView.as_view()), 
    path('control-inventario/<int:pk>/', ControlInventarioDetailView.as_view()),
]
