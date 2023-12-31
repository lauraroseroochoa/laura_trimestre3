from django.http import HttpRequest
from django.shortcuts import render
from . models import Usuario
from . forms import FormularioUsuario
from rest_framework import viewsets
from . serializer import UsuarioSerializer
# Create your views here.
# def usuariolist(request):
#     return render(request,'usuariolist.html')

def usuariolist(request):
    get_usuarios=Usuario.objects.all()
    data={
        'get_usuarios':get_usuarios
    }
    return render(request,'usuariolist.html',data)

def indexFormulario(request):
    usuario=FormularioUsuario()
    return render(request, "formusuario.html",{"form":usuario})

def procesarFormulario(request):
    
    if 'guardar' in request.POST:        
        usuario=FormularioUsuario(request.POST,request.FILES)
        if usuario.is_valid():
            usuario.save()
            usuario=FormularioUsuario()
        return render(request,"formusuario.html",{"form":usuario,"mensaje":"ok"} )

def editarUsuario(request,id_usuario):
    usuario=Usuario.objects.filter(id=id_usuario).first()
    form=FormularioUsuario(instance=usuario)
    return render(request, "UsuarioEdit.html",{"form":form,"usuario":usuario})

def actualizarUsuario(request,id_usuario):
    usuario=Usuario.objects.get(pk=id_usuario)
    form=FormularioUsuario(request.POST,instance=usuario)
    if form.is_valid():
       form.save()
       get_usuarios=Usuario.objects.all()
       return render(request,"usuariolist.html",{"get_usuarios":get_usuarios})
    
def eliminarUsuario(request, id_usuario):
    aprendiz=Usuario.objects.get(pk=id_usuario)
    aprendiz.delete()
    usuarios=Usuario.objects.all()
    return render(request, "usuariolist.html",{"get_usuarios":usuarios})

class UsuarioViewset(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
