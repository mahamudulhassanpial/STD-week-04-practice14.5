from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('add_student/', views.add_student, name="add_student"),
    path('delete/<int:roll>', views.delete_student, name="delete_student"),
]
