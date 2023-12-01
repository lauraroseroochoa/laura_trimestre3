from django.urls import path, include
from . import views
from rest_framework import routers
from . import views

router=routers.DefaultRouter()
router.register(r'admins',views.AdminView)

urlpatterns = [
    path('',include(router.urls)),
]
