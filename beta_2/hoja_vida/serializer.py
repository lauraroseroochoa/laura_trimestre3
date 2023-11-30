from rest_framework import serializers
from .models import Informacion_Person, Educacion, Empresa, Refe_personales, Refe_empresarial

class Hoja_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Informacion_Person
        fields=("__all__")

class EducacionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Educacion
        fields=("__all__")

class Hoja_EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Empresa
        fields=("__all__")

class Refe_personalesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Refe_personales
        fields=("__all__")
class Refe_empresarialSerializer(serializers.ModelSerializer):
    class Meta:
        model=Refe_empresarial
        fields=("__all__")