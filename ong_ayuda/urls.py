from django.contrib import admin
from django.urls import path
from .views import index,consulta,ubicacion

urlpatterns = [
    path('', index,name='IND'),
    path('consulta/<id>',consulta,name='CONS'),
    path('ubicacion/',ubicacion,name='UBI')
]
