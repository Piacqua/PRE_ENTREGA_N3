from django.urls import path
from . import views

urlpatterns = [
    path("nuestros-boxeadores/", views.Boxeadores, name="nuestros-boxeadores"),
    path("nuestros-entrenadores/", views.Entrenadores, name="nuestros-entrenadores"),
    path("nuestros-arbitros/", views.Arbitros, name="nuestros-arbitros"),
    path("registrate-boxeador/", views.Boxeadores_form, name="registrate-boxeador"),
    path(
        "registrate-entrenador/", views.Entrenadores_form, name="registrate-entrenador"
    ),
    path("registrate-arbitro/", views.Arbitros_form, name="registrate-arbitro"),
    path("busqueda-boxeador/", views.bbusqueda, name="busqueda-boxeador"),
    path("busqueda-arbitro/", views.abusqueda, name="busqueda-arbitro"),
    path("busqueda-entrenador/", views.ebusqueda, name="busqueda-entrenador"),
]
