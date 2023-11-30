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
    path('index/' , views.hoja_vida , name='index_hoja'),
    path('index/informacion', views.guardar_info , name='save_info'),
    path('index/educacion', views.guardar_educacion , name='save_educacion'),
    path('visualizar', views.visualizar_hoja , name='visualizar_hoja'),
    path('',include(router.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
