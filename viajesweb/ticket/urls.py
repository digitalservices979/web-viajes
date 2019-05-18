from django.urls import path
from .views import pasajero, CarListView, CarDeleteView

urlpatterns = [
    path('buy/<int:id_internacionale>/pasajero', pasajero, name='pasajero'),
    path('car_list', CarListView.as_view(), name='car_list'),
    path('<int:pk>/', CarDeleteView.as_view(), name='car_delete'),
]