from django.contrib import admin
from django.urls import path
from clientes.views import clientes_list
from clientes.views import clientes_delete
from clientes.views import clientes_new
from clientes.views import clientes_update


urlpatterns = [
    path('list/', clientes_list, name='clientes_list'),
    path('new/', clientes_new, name='clientes_new'),
    path('update/<int:id>', clientes_update, name='clientes_update'),
    path('delete/<int:id>', clientes_delete, name='clientes_delete'),
]