from django.urls import path, include
from . import views
from rest_framework import routers
from . import views

router=routers.DefaultRouter()
router.register(r'users',views.UsuarioView)

urlpatterns = [
    path('',include(router.urls)),
]
