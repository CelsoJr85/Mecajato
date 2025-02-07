from django.urls import path
from . import views

urlpatterns = [
    path('', views.clientes, name='clientes'),
    path('atualiza-cliente/', views.att_clientes, name='atualiza-clientes'),
]
