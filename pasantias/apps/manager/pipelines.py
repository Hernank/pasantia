# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from social.apps.django_app.default.models import UserSocialAuth
from apps.manager.models import Usuario
from apps.LN.ln import *
from urllib import urlopen
from django.template.defaultfilters import slugify
from django.core.files.base import ContentFile
import facebook
'''Login por redes sociales
PARAMETROS: backend - Desde donde me estoy logueando
 strategy -
 details - Retorna username, nombre, apellido
 response - Información del perfil
 user - objeto del usuario logueado
'''
def login(backend, strategy, details, response, user=None, *args, **kwargs):
    try:
        #Obtengo el id social por luego obtener el iduser
        id_social = response['id']
       
        User = get_user_model()

        #Obtengo el user id
        aus = UserSocialAuth.objects.get(uid=id_social)
        iduser = aus.user_id

        #Verifico si ya no existe el usuario, solamente lo crea si no existe
        us = User.objects.filter(pk=iduser)
        usuario=Usuario.objects.filter(pk=iduser)
        #Obtener ulr de perfil fallido
       # auth = us[0].social_auth.first()
        #graph = facebook.GraphAPI(auth.extra_data['access_token'])
       # fid = graph.get_object(id=auth.uid)
       # fid=fid['id']
       # miurllink='https://m.facebook.com/profile.php?id='+str(fid)
       # 
       # 
        
        if len(usuario) == 0:
            u=Usuario()
            u.rol='User'
            u.id=us[0].id 
            u.username=us[0].username#        
            u.first_name=details['first_name']
            u.last_name=details['last_name']
            u.email=details['email']
            u.password=(us[0].password) 
            url = "http://graph.facebook.com/%s/picture?type=large" % response['id']
            avatar = urlopen(url)
        
            u.imagenperfil.save(slugify(u.username + " social") + '.jpg', 
                            ContentFile(avatar.read())) 
            u.save()


        # u=Usuario()
         #   u.rol=usuario[0].rol
          #  u.id=iduser 
           # u.username=us[0].username#        
            #u.first_name=details['first_name']
            #u.last_name=details['last_name']
            #u.email=details['email']
            #u.password=(us[0].password) 
      
        #imagen avatar facebook 
        #url = "http://graph.facebook.com/%s/picture?type=large" % response['id']
        #avatar = urlopen(url)
        
        #u.imagenperfil.save(slugify(u.username + " social") + '.jpg', 
                           # ContentFile(avatar.read())) 
       # u.save()
       
     

        if us.count() == 0:
        #Verifico que tipo de backend es y obtengo el nombre de usuario
            if backend.name == 'facebook':
                surname = response["last_name"]
                name = response['first_name']
            elif backend.name == 'twitter':
                surname = response['name']
                name = ""
            else:
                return HttpResponseRedirect(reverse('url_de_logueo'))
           
           
            #Seteo que el usuario es del tipo usuario
            User.objects.filter(id=iduser).update(surname=surname,name=name)
        else:
            pass

           
            

    except Exception as ex:

        return HttpResponseRedirect(reverse('home'))