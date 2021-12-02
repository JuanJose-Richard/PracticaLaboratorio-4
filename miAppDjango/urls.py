
from django.urls import path, include

from . import views
from rest_framework import routers
#Rutas para la aplicacion no para el proyecto
#las comillas vacias son como la /
router = routers.DefaultRouter()
router.register(r'personas', views.PersonaViewSet)
urlpatterns = [
    path('',views.index, name='index'),
    path('persona/<int:persona_id>/', views.detail, name='detail'), 
    path('api/', include(router.urls))
]