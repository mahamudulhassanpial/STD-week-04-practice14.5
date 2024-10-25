from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('form/', views.submit_form, name = 'submit_form'),
    # path('form/', views.Input_forms, name = 'submit_form'),
    # path('django_form/', views.DjangoForm, name = 'django_form'),
    # path('django_form/', views.StudentForm, name = 'django_form'),
    path('django_form/', views.Geeks_Form, name = 'django_form'),
    # path('django_form/', views.Input_form, name = 'django_form'),
]