from django.urls import path
from . import views

urlpatterns = [
    path('products/',views.get_all_product , name = 'products'),
    path('products/<str:pk>/', views.get_by_id, name = 'get_by_id')
]