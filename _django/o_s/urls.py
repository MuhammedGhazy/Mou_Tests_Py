from . import views
from django.urls import path

urlpatterns = [
    
    path('home/', views.home),
    path('student/<st_id>', views.getStudent),
    path ('all/', views.getAll),
    path("new/", views.new_student),
    path('edit/<st_id>', views.editStudent),
    path('delete/<st_id>', views.Delete)
]