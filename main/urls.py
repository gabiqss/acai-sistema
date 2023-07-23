from django.urls import path
from . import views

urlpatterns = [
    path('', views.sorvete_pedido, name="pedido"),
    path('lista', views.pedidos, name='lista_pedidos'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
]