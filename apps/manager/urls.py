from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

#Recibe 'hola/','holavista' crear una url hola/ con vista holavista
def miurl(direccion,nombrevista):
    
    return url((r'^'+direccion+'$'), ('apps.manager.views.'+direccion),name=nombrevista)
#Recibe una direccion 'hola/' crea un visata hola
def miurl(direccion):
    obj=direccion.split('/')
    return url((r'^'+direccion+'$'), ('apps.manager.views.'+obj[-2]),name=obj[-2])

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pasantias.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^/', 'apps.manager.views.index',name='home'),
    miurl('verentrada/(.+)'),
    miurl('administracion/'),
    miurl('entradas/'),
    miurl('noticias/'),
    miurl('comentarios/'),
    miurl('categorias/'),
    miurl('usuarios/'),
    miurl('post/'),   
    miurl('crearunaentrada/'),    
    miurl('listarmisentradas/'),
    miurl('listarmisentradasfiltro/(.+)'),#Listar por categoria
    miurl('eliminarentrada/(.+)'),#elminarenrda por id entrada -Admin -User
    miurl('miperfil/'),#
    miurl('eliminarperfil/'),#eliminar perfil -Admin -User
    miurl('listarentradasbycat/(.+)'),#Listar entradas por categoria -Admin
    miurl('listarnoticias/'),#Listar todas las noticias -Admin
    miurl('crearnoticia/'),#Craer noticia -Admin
    miurl('editarnoticia/(.+)'),#Editar noticia  -Admin
    miurl('eliminarnoticia/(.+)'),#
    miurl('listarcategorias/'),# Listar todas las categoria -Admin
    miurl('crearcategoria/'),# Craer categoria -Admin
    miurl('editarcategoria/(.+)'),#Editar una categori por idcategoria
    miurl('eliminarcategoria/(.+)'),#
    miurl('listarusuarios/'),# Lista todos los usuarios -Admin
    miurl('eliminarusuario/(.+)'),#eliminar usaurio por idusuario -Admin
    miurl('miform/'),
    miurl('buscar/'),
    miurl('setrol/'),
    miurl('adduser/'),
    miurl('vercategoria/(.+)'),
    miurl('vercategoriac/(.+)'),
    miurl('vernoticias/'),
    miurl('getnoticia/'),
    miurl('cultura/'),
    #miurl('asignarrol/'),#_________
    url(r'^salir/$', 'apps.manager.views.logOut',name='logout'),
    url(r'^login/$', 'django.contrib.auth.views.login',{'template_name':'sbadmin/pages/login.html'},name='milogin'),
    url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login',name='milogout'),
    
)+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

