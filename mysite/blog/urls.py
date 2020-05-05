from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index, name='Index'),
    path('Home/', views.Home, name='Home'),
    path('Contact/', views.Contact, name='Contact'),
    path('Crud/', views.Crud, name='Crud'),
    path('NewsDate/<int:year>/', views.NewsDate, name='NewsDate')

]
