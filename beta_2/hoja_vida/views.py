from django.shortcuts import render , redirect
from . forms import Form_Info_Person , Form_educacion , Form_Empresa , Form_Refe_Person , Form_Refe_Empresarial
from . forms_disable import Form_Disable_Info_Person , Form_Disable_educacion , Form_Disable_Empresa , Form_Disable_Refe_Person , Form_Disable_Refe_Empresarial
from . models import Informacion_Person , Educacion , Empresa , Refe_personales , Refe_empresarial
from rest_framework import viewsets
from . serializer import Hoja_infoSerializer, EducacionSerializer, Hoja_EmpresaSerializer, Refe_empresarialSerializer, Refe_personalesSerializer
# Create your views here.
class Hoja_infoViewset(viewsets.ModelViewSet):
    queryset = Informacion_Person.objects.all()
    serializer_class = Hoja_infoSerializer

class EducacionViewset(viewsets.ModelViewSet):
    queryset = Educacion.objects.all()
    serializer_class = EducacionSerializer

class Hoja_EmpresaViewset(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = Hoja_EmpresaSerializer

class Refe_empresarialViewset(viewsets.ModelViewSet):
    queryset = Refe_empresarial.objects.all()
    serializer_class = Refe_empresarialSerializer

class Refe_personalesViewset(viewsets.ModelViewSet):
    queryset = Refe_personales.objects.all()
    serializer_class = Refe_personalesSerializer
