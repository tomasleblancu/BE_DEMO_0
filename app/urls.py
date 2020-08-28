from django.urls import path

from app import views

urlpatterns = [

    path('', views.Index, name='index'),

    path('servicios/', views.Servicios, name='servicios'),
    path('contacto/', views.Contacto, name='contacto'),

    path('login/', views.Login, name='login'),
    path('register/', views.Register, name='register'),
    path('logout/', views.Logout, name='logout'),

]