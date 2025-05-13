"""
URL configuration for libreria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from gestion_libros import views
from django.conf import settings
from django.conf.urls.static import static
from gestion_libros.views import (
    register_view,
    login_view,
    logout_view,
    index,
    alta_autor,
    listado_libros,
    nuevo_prestamo,
    crear_libro,
    listado_autores,
    registrar_usuario,
    listado_usuarios,
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path("",index , name='inicio'),
    path('alta_autor/', alta_autor, name='alta_autor'),
    path('listado_libros/', listado_libros,name='listado_libros'),
    path('nuevo_prestamo/', nuevo_prestamo, name='nuevo_prestamo'),
    path('crear_libro/', crear_libro, name='crear_libro'),
    path('autores/', listado_autores, name='listado_autores'),
    path('solicitar_prestamo/<int:libro_id>/', views.solicitar_prestamo, name='solicitar_prestamo'),
    path('solicitudes_pendientes/', views.listar_solicitudes_pendientes, name='solicitudes_pendientes'),
    path('procesar_solicitud/<int:solicitud_id>/<str:accion>/', views.procesar_solicitud, name='procesar_solicitud'),
    path('registrar-usuario/', registrar_usuario, name='registrar_usuario'),
    path('listado-usuarios/', listado_usuarios, name='listado_usuarios'),
    path('registrar-usuario/', registrar_usuario, name='registrar_usuario'),
    path('panel-bibliotecario/', views.panel_bibliotecario, name='panel_bibliotecario'),
    path('libros-prestados/', views.libros_prestados, name='libros_prestados'),
    path('libros-devueltos/', views.libros_devueltos, name='libros_devueltos'),

    # path('accounts/', include('django.contrib.auth.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
