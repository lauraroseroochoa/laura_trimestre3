from django.shortcuts import render , redirect
from . models import Usuario
from HumanTalentSena.static.python.encriptar import encriptar
from rest_framework import viewsets
from . serializer import UsuarioSerializer
# Create your views here.
class UsuarioView(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
