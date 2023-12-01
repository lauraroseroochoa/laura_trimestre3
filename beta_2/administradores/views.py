from django.shortcuts import render , redirect
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Admin
from HumanTalentSena.static.python.encriptar import encriptar
from .forms import FormularioAdmin
from rest_framework import viewsets
from . serializer import AdminSerializer

class AdminView(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
