from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from . import views

router=routers.DefaultRouter()
router.register(r'users',views.UsuarioViewset)
urlpatterns = [
    path('lista/', views.usuariolist,name='usuario_list'),
    path('indexFormulario/',views.indexFormulario,name="index_formulario"),
    path('procesarFormulario/',views.procesarFormulario,name="procesar_formulario"),
    path('editarusuario/<int:id_usuario>',views.editarUsuario,name="editar_usuario"),
    path("actualizar_usuario/<int:id_usuario>",views.actualizarUsuario, name="actualizar_usuario"),
    path("eliminar_usuario/<int:id_usuario>",views.eliminarUsuario, name="eliminar_usuario"),
    path('',include(router.urls)),
]