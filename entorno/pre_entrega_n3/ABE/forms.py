from django import forms
from django.db import models
from ABE.models import Boxeador, Arbitro, Entrenador


class Boxeador_Formulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    peso = forms.ChoiceField(required=True, choices=Boxeador.PESOS.choices)
    edad = forms.ChoiceField(required=True, choices=Boxeador.EDADES.choices)


class Entrenador_Formulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    edad = forms.IntegerField(required=True, max_value=99)
    experiencia = forms.ChoiceField(
        required=True, choices=Entrenador.EXPERIENCIA.choices
    )


class Arbitro_Formulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    edad = forms.IntegerField(required=True, max_value=99)
    experiencia = forms.ChoiceField(required=True, choices=Arbitro.EXPERIENCIA.choices)
