from django.urls import path

from . import views
#Rutas para la aplicacion no para el proyecto
#las comillas vacias son como la /
urlpatterns = [
    path('',views.index, name='index'),
    path('persona/<int:persona_id>/', views.detail, name='detail'), 
]