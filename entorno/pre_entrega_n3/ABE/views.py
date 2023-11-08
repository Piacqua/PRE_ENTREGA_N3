from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q

from ABE.forms import Boxeador_Formulario, Arbitro_Formulario, Entrenador_Formulario
from ABE.models import Boxeador, Entrenador, Arbitro


# Create your views here.
def Boxeadores(request):
    contexto = {"total_boxeadores": Boxeador.objects.all()}
    http_response = render(
        template_name="boxeadores.html", request=request, context=contexto
    )
    return http_response


def Entrenadores(request):
    contexto = {"total_entrenadores": Entrenador.objects.all()}
    http_response = render(
        template_name="entrenadores.html", request=request, context=contexto
    )
    return http_response


def Arbitros(request):
    contexto = {"total_arbitros": Arbitro.objects.all()}
    http_response = render(
        template_name="arbitros.html", request=request, context=contexto
    )
    return http_response


def Boxeadores_form(request):
    if request.method == "POST":
        formulario = Boxeador_Formulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            nombre = data["nombre"]
            peso = data["peso"]
            edad = data["edad"]

            boxeador = Boxeador(nombre=nombre, edad=edad, peso=peso)
            boxeador.save()  # Lo guardan en la Base de datos

            url_exitosa = reverse("nuestros-boxeadores")
            return redirect(url_exitosa)
    else:  # GET
        formulario = Boxeador_Formulario()
    http_response = render(
        request=request,
        template_name="form_boxeador.html",
        context={"formulario": formulario},
    )
    return http_response


def Entrenadores_form(request):
    if request.method == "POST":
        formulario = Entrenador_Formulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            nombre = data["nombre"]
            experiencia = data["experiencia"]
            edad = data["edad"]

            entrenador = Entrenador(nombre=nombre, edad=edad, experiencia=experiencia)
            entrenador.save()  # Lo guardan en la Base de datos

            url_exitosa = reverse("nuestros-entrenadores")
            return redirect(url_exitosa)
    else:  # GET
        formulario = Entrenador_Formulario()
    http_response = render(
        request=request,
        template_name="form_entrenador.html",
        context={"formulario": formulario},
    )
    return http_response


def Arbitros_form(request):
    if request.method == "POST":
        formulario = Arbitro_Formulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            nombre = data["nombre"]
            experiencia = data["experiencia"]
            edad = data["edad"]

            arbitro = Arbitro(nombre=nombre, edad=edad, experiencia=experiencia)
            arbitro.save()  # Lo guardan en la Base de datos

            url_exitosa = reverse("nuestros-arbitros")
            return redirect(url_exitosa)
    else:  # GET
        formulario = Arbitro_Formulario()
    http_response = render(
        request=request,
        template_name="form_arbitro.html",
        context={"formulario": formulario},
    )
    return http_response


def bbusqueda(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        bboxeador = Boxeador.objects.filter(
            Q(nombre__icontains=busqueda)
            | Q(edad__icontains=busqueda)
            | Q(peso__icontains=busqueda)
            | Q(peleas__icontains=busqueda)
            | Q(victorias__icontains=busqueda)
            | Q(derrotas__icontains=busqueda)
        )

        contexto = {
            "total_boxeadores": bboxeador,
        }
        http_response = render(
            request=request,
            template_name="boxeadores.html",
            context=contexto,
        )
        return http_response


def ebusqueda(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        bentrenador = Entrenador.objects.filter(
            Q(nombre__icontains=busqueda)
            | Q(edad__icontains=busqueda)
            | Q(experiencia__icontains=busqueda)
        )

        contexto = {
            "total_entrenadores": bentrenador,
        }
        http_response = render(
            request=request,
            template_name="entrenadores.html",
            context=contexto,
        )
        return http_response


def abusqueda(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        barbitro = Arbitro.objects.filter(
            Q(nombre__icontains=busqueda)
            | Q(edad__icontains=busqueda)
            | Q(experiencia__icontains=busqueda)
        )

        contexto = {
            "total_arbitros": barbitro,
        }
        http_response = render(
            request=request,
            template_name="arbitros.html",
            context=contexto,
        )
        return http_response
