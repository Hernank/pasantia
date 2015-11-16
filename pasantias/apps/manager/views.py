# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import HttpResponse
from django.core import serializers
from django.contrib.sites.models import Site
#Facebook
import datetime
from django.contrib.auth.models import User
from apps.manager.models import FacebookStatus
import facebook
from django.template import defaultfilters
from django.conf import settings
import urllib2
from apps.LN.ln import *
import json 
import re
# Create your views here.
# 
# 
def postear(entrada,user):
	
	resumencorto=entrada.resumen+"...."
	if len(resumencorto)>50:
		resumencorto=resumencorto[:50]+" ..."
	urlimagen=settings.MI_DOMINIO+"/verentrada/"+str(entrada.id_entrada)
	attachment =  {
	'name': entr.titulo,
	'link': urldelaentrada,
	'caption': 'Categoria: '+entr.categoria.nombre,
	'description': resumencorto,
	'picture': urlimagen
	}
	mimessage="Me parece un libro interesante : "+entr.titulo 
	mimessage2="Me parece un libro interesante : "+entr.titulo+"  #BLU" #Parael mensaje de publicacion en la pagina de facebook
	#POSTEAR EN MI PERFI:
	auth = request.user.social_auth.first()
	graph = facebook.GraphAPI(auth.extra_data['access_token'])
	graph.put_wall_post(message=mimessage2, attachment=attachment)
	#POSTEAR EN LA PAGINA DE BLU
	attachment =  {
	'page_token' :str('CAAJ1YL4mF38BAEoOEBySOuv6LJfxKt1u0iwRKH6U6Du67pnG7ne9NOHfhJDQ0ZAQbSrBVxbdW94EmT7pDBlW2XFiUqBCA0kBlHZBOshwWUMFsd3tD8JyjqAcLKdd2Wo3UAl7StE5nItZAawFRSIN6d7UOcSJZCm91ZCx5hYTZCjXOvgslO3SsNMNcO21gzGoRz1wI1ZBjx4tQZDZD'),
	'name': entr.titulo,
	'link': urldelaentrada ,
	'caption':'Categoria: '+entr.categoria.nombre, 
	'description': resumencorto,
	'picture': urlimagen , 
	}
	post = graph.put_wall_post(message=mimessage2, attachment=attachment,profile_id=str(356590257795063))


def indexasa(request):
	
	rol=''
	if Admin.estaLogueado(request.user):
		rol=Admin.usergetrol(request.user)

	template='manager/index.html'
	miscategorias=Categorialn.getcategorias()
	listasort=Categorialn.getcategoriassort(3)
	noticias=Noticialn.getnoticias()
	ctx={'categorias':miscategorias,'listasort':listasort,'noticias':noticias,}
	return render(request,template,ctx)
	
def setrosdl(request):	
	iduser = int(request.GET['iduser'])
	rol = str(request.GET['rol'])
	Userln.setrol(iduser, rol)
	payload = {'okk': 'ok'}
	return HttpResponse(json.dumps(payload), content_type='application/json')


def crearunaentrada(request):
	
	try:
		
		titulo=request.GET['titulo']
		resumen=request.GET['resumen']
		imagen=request.FILES['imagenlibrourl']
		imagen2=request.FILES.get('imagenlibropdf')
		libropdf=request.FILES.get('pdflibro')
		librourl=str(request.GET['urllibro'])
		wantpost=request.POST.get('wantpost')
		wantpost=wantpost is not None
		categoria=Categorialn.getcategoria(int(request.POST['categorias']))
			
		#user=User.objects.get(pk=7)#request.user
		user=request.user
		payload = {'error': True,'mensaje':'Este es mi mensaje'}
		return HttpResponse(json.dumps(payload), content_type='application/json')
		pass
	except Exception, e:
		raise
	else:
		pass
	finally:
		pass

	ctx={'':'',}
	return render(request,template,ctx)


def index(request):
	
	rol=''
	if Admin.estaLogueado(request.user):
		rol=Admin.usergetrol(request.user)

	template='manager/index.html'
	miscategorias=Categorialn.getcategorias()
	listasort=Categorialn.getcategoriassort(3)
	noticias=Noticialn.getnoticias()
	ctx={'categorias':miscategorias,'listasort':listasort,'noticias':noticias,}
	
	if request.method=='POST':
		wantpost=False
		#if Admin.estaLogueado(request.user) and Admin.esAdmin
		#
		try:
			titulo=request.POST['titulo']
			resumen=request.POST['resumen']
			imagen=request.FILES.get('imagenlibrourl')
			imagen2=request.FILES.get('imagenlibropdf')
			libropdf=request.FILES.get('pdflibro')
			librourl=str(request.POST['urllibro'])
			wantpost=request.POST.get('wantpost')
			wantpost=wantpost is not None
			categoria=Categorialn.getcategoria(int(request.POST['categorias']))
			
			#user=User.objects.get(pk=7)#request.user
			user=request.user
			entr=Entrada()
			entr.resumen=resumen
			entr.titulo=titulo
			
			entr.categoria=categoria
			entr.autor=user
			entr.libro=libropdf
			
			esurl=imagen is not None and (librourl is not "" or len(librourl)>7)  
			espdf=libropdf is not None and imagen2 is not None 
			valido=False
			if espdf:
				entr.imagen_libro=imagen2	
				entr.libro=libropdf			
				valido=True

			elif esurl:
				entr.imagen_libro=imagen
				ret = urllib2.urlopen(str(librourl))
				if ret.code == 200:
					print "Exists!"
					if librourl[-4:]=='.pdf' or librourl[-4:]=='.PDF':
						entr.librourl=librourl
						valido=True
				
			
		
			if rol=='AdminCultura':
				entr.tag='Cultura'

			#entr.fecha_publicacion=datetime.datetime.now()
			

			#Post en facebook
			user =user		
			#status = nuevopost
			#graph.put_object('me', 'feed', message=status.message)
			#status.publish_timestamp = datetime.datetime.now()
			#status.save()
			#
								
			if wantpost:
				postear(entr, request.user)		
			if 	valido:
				entr.save()
				return redirect('/verentrada/'+str(entr.id_entrada))
			else:
				return redirect("/")

		except Exception as  ex:
			print "Error: Execpcion no controlada : "+ex.message
		
		finally:
			pass
		
		


	else:
		pass
	return render(request,template,ctx)

def obtener(lista,cantidad):
	if len(lista)<=cantidad: 
		return lista
	else:
		return lista[:cantidad]
def administracion(request):

	if not Admin.estaLogueado(request.user):
		return redirect('/')
	
	rol=Admin.usergetrol(request.user )
	if rol=='User':
		return redirect('/')
	entradas=''
	noticias=''
	categorias=''
	usuarios=''
	if rol=='Admin':
		entradas=(Entradaln.getentradas())  
		categorias=(Categorialn.getcategorias())
		noticias=(Noticialn.getnoticias())
		usuarios=(Userln.getusers())
	if rol=='AdminCultura':	
		entradas=(Entradaln.getentradascultura())
		categorias=(Categorialn.getcategoriascultura())	
		noticias=(Noticialn.getnoticiascultura()) 
	
	template='manager/admin.html'
	ctx={'lenentradas':len(entradas),'lennoticias':len(noticias),'lencategorias':len(categorias),'lenusuarios':len(usuarios),
	'entradas':obtener(entradas,5),'noticias':obtener(noticias,5),'categorias':obtener(categorias,5),'usuarios':obtener(usuarios,5),
	}
	return render(request,template,ctx)


def entradas(request):
	if not Admin.estaLogueado(request.user):
		return redirect('/')
	
	if Admin.esUser(request.user):
		return redirect('/')
	rol=Admin.usergetrol(request.user)
	entradas=''
	if rol=='AdminCultura':
		entradas=Entradaln.getentradascultura()
	else: 
		entradas=Entradaln.getentradas()
	template='manager/entradas.html'
	ctx={'entradas':entradas,}
	return render(request,template,ctx)


	
def categorias(request):
	if not Admin.estaLogueado(request.user):
		return redirect('/')
	rol=Admin.usergetrol(request.user) 
	categorias=''

	if Admin.esUser(request.user):
		return redirect('/')
	if rol=='AdminCultura' : 
		categorias=Categorialn.getcategoriascultura()
	if rol=='Admin': 
		categorias=Categorialn.getcategorias()
	template='manager/categorias.html'
	
	ctx={'categorias':categorias,}
	return render(request,template,ctx)
def listarnoticias(request):
	template='manager/listarnoticias.html'
	
	return render(request,template,ctx)
def comentarios(request):
	if not Admin.estaLogueado(request.user):
		return redirect('/')
	
	if Admin.esUser(request.user):
		return redirect('/')
	template="manager/comentarios.html"
	ctx={"":"",}
	return render(request,template,ctx)
def usuarios(request):
	if not Admin.estaLogueado(request.user):
		return redirect('/')
	
	if Admin.esUser(request.user):
		return redirect('/')
	template='manager/usuarios.html'
	users=Userln.getusers()
	roles=['User','Admin','AdminCultura']
	ctx={'users':users,'roles':roles,}
	return render(request,template,ctx)

def post(request):
	ctx={'jose':'heranna',}
	return (request,'',ctx)
	


def listarmisentradas(request):
	template='manager/listarmisentradas.html'
	entradas=Entradaln.getentradasbyuser(request.user)
	ctx={'entradas':entradas,}
	return render(request,template,ctx)

def listarmisentradasfiltro(request,id_categoria):
	template='manager/listarmisentradasfiltro.html'
	ctx={'':'',}
	return render(request,template,ctx)

def eliminarentrada(request,id_entrada):
	if not Admin.estaLogueado(request.user):
		return redirect('/')
	rol=Admin.usergetrol(request.user)
	user=Userln.getuser(request.user.id)
	entrada=Entradaln.getentrada(id_entrada)
	if rol=='User':
		if entrada.autor.id==user.id:
			Entradaln.eliminarentrada(id_entrada)	
			return redirect('/entradas')
	if rol=='AdminCultura' and Entradaln.getentrada(id_entrada).tag=='Cultura':
		Entradaln.eliminarentrada(id_entrada)
	
	#OJO si es AdminCultura elimnar su entradas
	template='manager/eliminarentrada.html'
	
	
	if rol=='Admin':
		Entradaln.eliminarentrada(id_entrada)	
	
	ctx={'':'',}

	return redirect('/entradas')
	

def miperfil(request):
	template='manager/miperfil.html'
	ctx={'':'',}
	return render(request,template,ctx)

def eliminarperfil(request):
	template='manager/eliminarperfil.html'
	ctx={'':'',}
	return render(request,template,ctx)

def listarentradasbycat(request,id_categoria):
	template='manager/listarentradasbycat.html'
	ctx={'':'',}
	return render(request,template,ctx)

def noticias(request):

	if not Admin.estaLogueado(request.user):
		return redirect('/')
	rol=Admin.usergetrol(request.user)
	if rol=='User':
		return redirect('/')
	template='manager/noticias.html'
	noticias=''
	if rol=='AdminCultura':
		noticias=Noticialn.getnoticiascultura()
	if rol=='Admin':
		noticias=Noticialn.getnoticias()
	
	if request.method=='POST':
		try:
			titulo=request.POST['titulonoticia']
			descripcion=request.POST['descripcionnoticia']
			imagen=request.FILES['imagennoticia']	
			user=Userln.getuser(request.user.id)
			noticia=Noticia()
			noticia.contenido=descripcion
			noticia.titulo=titulo
			noticia.imagen_noticia=imagen		
			noticia.autor=user
			if rol=='AdminCultura':
				noticia.tag='Cultura'
			noticia.save()

			# #Post en facebook
			# user =user
			# nuevopost=FacebookStatus()
			# nuevopost.author=user 
			# nuevopost.status='approved'
			# nuevopost.link='https://www.facebook.com'
			# nuevopost.message="Este es mi mensaje"

			# status = nuevopost
			
			# resumencorto=entr.resumen+"..."
			# if len(resumencorto)>50:
			# 	resumencorto=resumencorto[:50]+"..."
			# 
			# urlimagen=str(Site.objects.get_current().domain+':8000'+entr.imagen_libro.url)
			# urldelaentrada=str(Site.objects.get_current().domain+':8000')+'/verentrada/'+str(entr.id_entrada)
			# attachment =  {
	  #   	'name': entr.titulo,
	  #   	'link': urldelaentrada,
	  #   	'caption': 'Categoria: '+entr.categoria.nombre,
	  #   	'description': resumencorto,
	  #  	  	'picture': urlimagen
			# }
			# mimessage="Me parece un libro interesante : "+entr.titulo 
			# mimessage2="Me parece un libro interesante : "+entr.titulo+"  #BLU" 
			# #POSTEAR EN MI PERFI:
			# graph.put_wall_post(message=mimessage2, attachment=attachment)
			# #POSTEAR EN LA PAGINA DE BLU
			# attachment =  {
			# 'page_token' :str('CAAJ1YL4mF38BAEoOEBySOuv6LJfxKt1u0iwRKH6U6Du67pnG7ne9NOHfhJDQ0ZAQbSrBVxbdW94EmT7pDBlW2XFiUqBCA0kBlHZBOshwWUMFsd3tD8JyjqAcLKdd2Wo3UAl7StE5nItZAawFRSIN6d7UOcSJZCm91ZCx5hYTZCjXOvgslO3SsNMNcO21gzGoRz1wI1ZBjx4tQZDZD'),
			#  'name': entr.titulo,
			#   'link': urldelaentrada ,
			#   'caption':'Categoria: '+entr.categoria.nombre, 
			#   'description': resumencorto,
			#   'picture': urlimagen , 
			# }
			# post = graph.put_wall_post(message=mimessage2, attachment=attachment,profile_id=str(356590257795063))
			# 
		except Exception as e:
			print e.message
		finally:
			pass
		
	else:
		pass

	
	ctx={'noticias':noticias,}
	return render(request,template,ctx)

def crearnoticia(request):
	template='manager/crearnoticia.html'
	ctx={'':'',}
	return render(request,template,ctx)

def editarnoticia(request,id_noticia):
	template='manager/editarnoticia.html'
	ctx={'':'',}
	return render(request,template,ctx)

def eliminarnoticia(request,id_noticia):
	template='manager/eliminarnoticia.html'

	if not Admin.estaLogueado(request.user):
		return redirect('/')

	rol=Admin.usergetrol(request.user)
	if rol=='User':
		return redirect('/')
	if rol=='AdminCultura' and Noticialn.getnoticia(id_noticia).tag=='Cultura':  
		Noticialn.eliminarnoticia(id_noticia)

	if rol=='Admin':
		Noticialn.eliminarnoticia(id_noticia)

	ctx={'':'',}
	return redirect('/noticias')

def listarcategorias(request):
	template='manager/listarcategorias.html'
	ctx={'':'',}
	return render(request,template,ctx)

def crearcategoria(request):
	if not Admin.estaLogueado(request.user):
		return redirect('/')

	rol=Admin.usergetrol(request.user)
	if rol=='User':
		return redirect('/')

	template='manager/crearcategoria.html'
	if rol=='AdminCultura':
		Categorialn.crearcategoriacultura(request.POST['nombrecategoria'])
	if rol=='Admin':
		Categorialn.crearcategoria(request.POST['nombrecategoria'])
	ctx={'':'',}
	return redirect('/categorias')

def editarcategoria(request,id_categoria):
	if not Admin.estaLogueado(request.user):
		return redirect('/')
	rol=Admin.usergetrol(request.user)
	if rol=='User':
		return redirect('/')

	template='manager/editarcategoria.html'
	ctx={'':'',}
	if request.method=='POST':		
		nombre=request.POST['nombrecategoria']
		cate=Categorialn.getcategoria(id_categoria)
		cate.nombre=nombre
		cate.save()
		return redirect("/categorias/")

	else:
		pass
	return redirect("/categorias/")

def eliminarcategoria(request,id_categoria):
	import pdb; pdb.set_trace()
	if not Admin.estaLogueado(request.user):
		return redirect('/')

	rol=Admin.usergetrol(request.user)
	if rol=='User':
		return redirect('/')
	if rol=='AdminCultura' and Categorialn.getcategoria(id_categoria).tag=='Cultura':
		Categorialn.eliminarcategoriacultura(id_categoria)
	if rol=='Admin':
		Categorialn.eliminarcategoria(id_categoria)
	template='manager/eliminarcategoria.html'
	ctx={'':'',}
	
	return redirect("/categorias")

def listarusuarios(request):
	template='manager/listarusuarios.html'
	ctx={'':'',}
	return render(request,template,ctx)

def eliminarusuario(request,id_usuario):
	template='manager/eliminarusuario.html'
	
	Admin.eliminaruser(id_usuario)
	ctx={'':'',}
	return redirect('/usuarios/')


def logOut(request):	
	logout(request)
	return redirect('/')


	
def verentrada(request,identrada):
	
	template='manager/verentrada.html'

	entrada=Entradaln.getentrada(int(identrada))
	ctx={'entrada':entrada,'eliminar':False}
	if Admin.estaLogueado(request.user):
		
		if entrada.autor.id==request.user.id:
			ctx={'entrada':entrada,'eliminar':True}

	return render(request,template,ctx)

import datetime

def miform(request):
	
	template='miform.html'
	ctx={'':'',}
	if request.method=='POST':
		
		titulo=request.POST['titulo']
		resumen=request.POST['resumen']
		imagen=request.FILES['file']
		categoria=Categorialn.getcategoria(4)
		user=User.objects.get(pk=4)
		entr=Entrada()
		entr.resumen=resumen
		entr.titulo=titulo
		entr.imagen_libro=imagen
		entr.categoria=categoria
		entr.autor=user
		entr.fecha_publicacion=datetime.datetime.now()
		entr.save()

	else:
		pass

	return render(request,template,ctx)

	
def vercategoria(request,id_categoria):
	template="manager/vercategoria.html"
	entradas=Entradaln.getentradasbycategoria(id_categoria)
	ctx={'entradas':entradas,}
	return render(request,template,ctx)
def vercategoriac(request,id_categoria):
	template="manager/vercategoriac.html"
	entradas=Entradaln.getentradasbycategoriacultura(id_categoria)
	ctx={'entradas':entradas,'ctxxcategorias':miscategoriass()}
	return render(request,template,ctx)

	

def vernoticias(request):
	limite=10
	template="manager/vernoticias.html"
	noticias=Noticialn.getnoticias()
	noticiaslen=noticias
	miscategoriass=Categorialn.getcategorias()
	if len(noticias)>limite:
		noticiaslen=noticiaslen[:limite]

	ctx={'noticiaslen':noticiaslen,'noticias':noticias,'categorias':miscategoriass,}
	return render(request,template,ctx)

def buscar(request):
	
	template="manager/buscar.html"
	busqueda=''
	busqueda=request.POST['buscar']
	s=Entradaln.buscar(busqueda)
	ctx={'entradas':s,}
	return render(request,template,ctx)

def setrol(request):	
	iduser = int(request.GET['iduser'])
	rol = str(request.GET['rol'])
	Userln.setrol(iduser, rol)
	payload = {'okk': 'ok'}
	return HttpResponse(json.dumps(payload), content_type='application/json')


def getnoticia(request):
	
	id_noticia = int(request.GET['idnoticia'])
	noticia =Noticialn.getnoticia(id_noticia)
	
	try:
		fecha=noticia.fecha_publicacion.strftime('Publicado en %d, %b %Y')
		noticiaa={'titulo':noticia.titulo,'contenido':noticia.contenido,'imagen':noticia.imagen_noticia.url,'fecha':fecha}
	
	except Exception as e:
		i=5
		print e.message
	else:
		pass
	finally:
		pass
	#data=serializers.serialize('json', [noticia,])
	return HttpResponse(json.dumps(noticiaa), content_type='application/json')

def miscategoriass():
	
	allcategorias=Categorialn.getcategorias()
	milista=[]
	for i in allcategorias:
		count=Categorialn.getcountcategoriacultura(i.id_categoria)
		if count!=0:
			milista.append({'categoria':i,'len':count})	

	
	milista.sort( key=lambda milen: milen['len'],reverse=True)  
	return milista

def cultura(request):
	
	template='manager/cultura.html'
	miscategorias=Categorialn.getcategorias()
	listasort=Categorialn.getcategoriassortcultura(3)
	ultimasent=Entradaln.ultimasentradascultura(4)
	noticias=obtener(Noticialn.getnoticiascultura(),1)
	ctx={'categorias':miscategorias,'listasort':listasort,'noticias':noticias,'ctxxcategorias':miscategoriass(),'lastentradasc':ultimasent}
	if request.method=='POST':
		#if Admin.estaLogueado(request.user) and Admin.esAdmin
		#
		titulo=request.POST['titulo']
		resumen=request.POST['resumen']
		imagen=request.FILES['file1']
		libro=request.FILES['file2']
		categoria=Categorialn.getcategoria(int(request.POST['categorias']))
		#user=User.objects.get(pk=7)#request.user
		user=request.user
		entr=Entrada()
		entr.resumen=resumen
		entr.titulo=titulo
		entr.imagen_libro=imagen
		entr.categoria=categoria
		entr.autor=user
		entr.libro=libro
		#entr.fecha_publicacion=datetime.datetime.now()
		entr.save()

		#Post en facebook
		user =user
		nuevopost=FacebookStatus()
		nuevopost.author=user 
		nuevopost.status='approved'
		nuevopost.link='https://www.facebook.com'
		nuevopost.message="Este es mi mensaje"

		status = nuevopost

		

		#graph.put_object('me', 'feed', message=status.message)
		#status.publish_timestamp = datetime.datetime.now()
		#status.save()
		resumencorto=entr.resumen+"..."
		if len(resumencorto)>50:
			resumencorto=resumencorto[:50]+"..."
		
		urlimagen=str(Site.objects.get_current().domain+':8000'+entr.imagen_libro.url)
		urldelaentrada=str(Site.objects.get_current().domain+':8000')+'/verentrada/'+str(entr.id_entrada)
		attachment =  {
    	'name': entr.titulo,
    	'link': urldelaentrada,
    	'caption': 'Categoria: '+entr.categoria.nombre,
    	'description': resumencorto,
   	  	'picture': urlimagen
		}
		mimessage="Me parece un libro interesante : "+entr.titulo 
		mimessage2="Me parece un libro interesante : "+entr.titulo+"  #BLU" 
		#POSTEAR EN MI PERFI:
		graph.put_wall_post(message=mimessage2, attachment=attachment)
		#POSTEAR EN LA PAGINA DE BLU
		attachment =  {
		'page_token' :str('CAAJ1YL4mF38BAEoOEBySOuv6LJfxKt1u0iwRKH6U6Du67pnG7ne9NOHfhJDQ0ZAQbSrBVxbdW94EmT7pDBlW2XFiUqBCA0kBlHZBOshwWUMFsd3tD8JyjqAcLKdd2Wo3UAl7StE5nItZAawFRSIN6d7UOcSJZCm91ZCx5hYTZCjXOvgslO3SsNMNcO21gzGoRz1wI1ZBjx4tQZDZD'),
		 'name': entr.titulo,
		  'link': urldelaentrada ,
		  'caption':'Categoria: '+entr.categoria.nombre, 
		  'description': resumencorto,
		  'picture': urlimagen , 
		}
		post = graph.put_wall_post(message=mimessage2, attachment=attachment,profile_id=str(356590257795063))




	else:
		pass
	return render(request,template,ctx)
def validarcorreo(correo):	
	if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correo.lower()):
		return True
	else:
		print False

def adduser(request):
	import pdb; pdb.set_trace()
	
	username=str(request.GET['username'])
	nombre=str(request.GET['nombre'])
	apellido=str(request.GET['apellido'])
	correo =str(request.GET['correo'])

	password1=str(request.GET['password1'])
	password2=str(request.GET['password2'])
	error=False
	mensaje="Registro de usuario exitoso"
	if Userln.existethisusername(username):
		error=True
		mensaje="Ya existe este usuario"
	if not (password1==password2):
		error=True
		mensaje='Las password deben ser iguales'
	if not validarcorreo(correo):
		error=True
		mensaje='Ingrese un correo valido'
	payload = {'error': error,'mensaje':mensaje}
	if error:		
		return HttpResponse(json.dumps(payload), content_type='application/json'	)
	
	user=Usuario()
	user.first_name=nombre
	user.last_name=apellido
	user.rol='User'
	user.set_password(password1)
	user.email=correo
	user.username=username
	user.save()
	return HttpResponse(json.dumps(payload), content_type='application/json'	)
	
	