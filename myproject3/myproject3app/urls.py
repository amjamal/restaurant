from . import views
from django.urls import path
app_name = 'myproject3app'

urlpatterns = [
    path('', views.rest, name='restaurant'),
    path('viande/', views.viande, name='viande'),
]