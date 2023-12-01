from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'hoja',views.Hoja_infoViewset)
router.register(r'hoja2', views.EducacionViewset)
router.register(r'hoja3', views.Hoja_EmpresaViewset)
router.register(r'hoja4', views.Refe_empresarialViewset)
router.register(r'hoja5', views.Refe_personalesViewset)

urlpatterns = [
    path('',include(router.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
