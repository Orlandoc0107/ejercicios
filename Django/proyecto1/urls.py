
from django.contrib import admin
from django.urls import path
from . import views
#from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludos/', views.saludo, name='saludos'),#ruta estaticas
    path('despedida/', views.despedida, name='despedida'),
    path('adulto/<int:edad>/', views.adulto, name='adulto')

]
