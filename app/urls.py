from django.urls import path

from app import views

urlpatterns = [
    
    path('', views.Home, name="Home"),
    path('Servicios', views.Servicios, name="Servicios"),
    path('Discipulado', views.Discipulado, name="Discipulado"),
    path('Libros', views.Libros, name="Libros"),
    path('Biblias', views.Biblias, name="Biblias"),
    path('Galeria', views.Galeria, name="Galeria"),
    path('Contacto', views.Contacto, name="Contacto"),
    
]