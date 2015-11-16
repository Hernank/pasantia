#encoding:UTF-8
from django.contrib.auth.models import User
from apps.manager.models import *
from django.db.models import Q
class Excepcion(Exception):
	def __init__(self, valor):
		self.valor = valor
	def __str__(self):
		return repr(self.valor)

# >>> try:
# ...     raise MiError(2*2)
# ... except MyError as e:
# ...     print('Ocurrió mi excepción, valor:', e.valor)
class Admin(object):
	"""docstring for Admin
		Recibe django.contrib.auth.models.User
	"""
	def __init__(self, arg):
		super(Admin, self).__init__()
		self.arg = arg

	@staticmethod
	def estaLogueado(user):
		return user.is_authenticated()
	@staticmethod  
	def esAnonimo(user):
		return  user.is_anonymous()
	@staticmethod  
	def esAdmin(user):
		user=Usuario.objects.get(pk=user.id)
		return user.rol=='Admin' or user.rol ==''
	
	@staticmethod  
	def esUser(user):
		user=Usuario.objects.get(pk=user.id)
		return user.rol=='User'
	@staticmethod 
	def eliminaruser(id_user):
		user=User.objects.get(pk=id_user)
		user.is_active=not user.is_active
		user.save()
	@staticmethod 
	def usergetrol(user):
		user=Usuario.objects.get(pk=user.id)
		return user.rol



class Entradaln(object):
	"""docstring for Entrada"""
	def __init__(self, arg):
		super(Entrada, self).__init__()
		self.arg = arg

	@staticmethod  	
	def getentradasbyuser(user):
		entradas=Entrada.objects.filter(autor__pk=user.id).order_by('-fecha_publicacion')

		return entradas
	@staticmethod  
	def getentradas():		
		#Return todas las entradas
		
		entradas=Entrada.objects.all().order_by('-fecha_publicacion')
		
		return entradas
	@staticmethod  
	def getentradascultura():		
		#Return todas las entradas
		
		entradas=Entrada.objects.filter(tag='Cultura').order_by('-fecha_publicacion')
		
		return entradas
		
	@staticmethod 
	def getentradasbycategoria(id_categoria):	
		try:
			pass
		except Exception as ex:
			raise Excepcion("Error: Excepcion no controlada : "+ex.message)
		except Excepcion as ex:
			raise ex
		finally:
			pass
		
		#Retorna entradas de una categoria
		id_categoria=int(id_categoria)
		entradas=Entrada.objects.filter(categoria=id_categoria).order_by('-fecha_publicacion')
		return entradas

	


	@staticmethod 
	def getentradasbycategoriacultura(id_categoria):	
		try:
			pass
		except Exception as ex:
			raise Excepcion("Error: Excepcion no controlada : "+ex.message)
		except Excepcion as ex:
			raise ex
		finally:
			pass
		
		#Retorna entradas de una categoria
		id_categoria=int(id_categoria)
		entradas=Entrada.objects.filter(categoria=id_categoria,tag='Cultura').order_by('-fecha_publicacion')
		return entradas


	@staticmethod  
	def getentrada(id_entrada):
		try:
			entra=Entrada.objects.get(pk=id_entrada)
			return entra			
		except Excepcion as ex:
			raise ex	
		except DoesNotExist:
			raise Excepcion("Error: Esta clave no existe :"+id_entrada)
		except Exception as ex:
			raise  Excepcion("Error: Excepcion no controlada : "+ex.message)
		finally:
			pass
		
	@staticmethod
	def setentradascatdefault(id_categoria):
		try:
			
			id_categoria=int(id_categoria)
			entradas=Entradaln.getentradasbycategoria(id_categoria)
			default=Categoria.objects.get(pk=1)
			for i in entradas:
				i.categoria=default
				i.save()
			return True

		except Exception as ex:
			raise Excepcion("Error: Excepcion no controlada : "+ex.message)
		except Excepcion as ex:
			raise ex
		finally:
			pass

	@staticmethod
	def setentradascatdefaultcultura(id_categoria):
		try:
			
			id_categoria=int(id_categoria)
			entradas=Entradaln.getentradasbycategoria(id_categoria)
			default=Categoria.objects.get(pk=2)
			for i in entradas:
				i.categoria=default
				i.save()
			return True

		except Exception as ex:
			raise Excepcion("Error: Excepcion no controlada : "+ex.message)
		except Excepcion as ex:
			raise ex
		finally:
			pass
	@staticmethod
	def ultimasentradas(numerodeentradas):
		ent=Entradaln.getentradas().order_by('-fecha_publicacion')
		if len(ent)<numerodeentradas:
			return ent
		return ent[:numerodeentradas]
	@staticmethod
	def ultimasentradascultura(numerodeentradas):
		ent=Entradaln.getentradascultura().order_by('-fecha_publicacion')
		if len(ent)<numerodeentradas:
			return ent
		return ent[:numerodeentradas]


	@staticmethod 
	def eliminarentrada(id_entrada):
		try:
			id_entrada=int(id_entrada)
			nt=Entradaln.getentrada(id_entrada)
			nt.delete()
		except Exception as  e:
			raise Excepcion("Error: Execpcion no controlada : "+e.message)
		except Excepcion as ex:
			raise ex
		finally:
			pass

	@staticmethod 
	def buscar(busqueda):
		query = busqueda
		results=''
		if query:
			qset = (Q(titulo__icontains=query) |Q(resumen__icontains=query) )
			results = Entrada.objects.filter(qset).distinct().order_by('-fecha_publicacion')
		else:
			results = []
		return results
	
		
class Noticialn(object):
	"""docstring for Noticia"""
	def __init__(self, arg):
		super(Noticia, self).__init__()
		self.arg = arg
	@staticmethod  
	def getnoticias():
		nts=Noticia.objects.all().order_by('-fecha_publicacion')
		
		return nts
	@staticmethod  
	def getnoticia(id_noticia):
		try:
			id_noticia=int(id_noticia)
			nt=Noticia.objects.get(pk=id_noticia)
			return nt
		except Exception as  ex:
			raise Excepcion("Error: Execpcion no controlada : "+ex.message)
		except DoesNotExist as e:
			raise Excepcion("Error: No existe el id de noticia : "+id_noticia+" - "+e.message)
		finally:
			pass
		
	@staticmethod
	def eliminarnoticia(id_noticia):
		try:
			id_noticia=int(id_noticia)
			nt=Noticia.objects.get(pk=id_noticia)
			nt.delete()
		except Exception as  e:
			raise Excepcion("Error: Execpcion no controlada : "+e.message)
		except Excepcion as ex:
			raise ex
		finally:
			pass
	@staticmethod 
	def getnoticiascultura():
		try:
			
			nt=Noticia.objects.filter(tag="Cultura").order_by('-fecha_publicacion')
			return nt
		except Exception as  e:
			raise Excepcion("Error: Execpcion no controlada : "+e.message)
		except Excepcion as ex:
			raise ex
		finally:
			pass
		
class Categorialn(object):
	"""docstring for Categoria"""
	def __init__(self, arg):
		super(Categoria, self).__init__()
		self.arg = arg
	@staticmethod 
	def crearcategoria(nombre):
		categoria=Categoria()
		categoria.nombre=nombre
		categoria.save()
	@staticmethod
	def crearcategoriacultura(nombre):
		categoria=Categoria()
		categoria.nombre=nombre
		categoria.tag='Cultura'
		categoria.save()	
	@staticmethod  
	def getcategorias():		
		categ=Categoria.objects.all();

		return categ		
		
	@staticmethod  
	def getcategoriascultura():		
		categ=Categoria.objects.filter(tag='Cultura');

		return categ		
	
	@staticmethod 
	def eliminarcategoria(id_categoria):
		try:
			
			id_categoria=int(id_categoria)
			cats=Categorialn.getcategorias()
			if int(id_categoria)==1:
				raise Excepcion("Error: No se puede eliminar la categoria por default")
			if len(cats)>=2 :
				Entradaln.setentradascatdefault(id_categoria)
			cate=Categorialn.getcategoria(id_categoria)
			cate.delete()
			#elimino la categoria
			return True
		except Exception as ex:
			raise Excepcion("Error: excepcion no controlada : "+ex.message)
		except Excepcion as ex:
			raise ex
		finally:
			pass	
	@staticmethod 
	def eliminarcategoriacultura(id_categoria):
		try:
			
			id_categoria=int(id_categoria)
			cats=Categorialn.getcategorias()
			if int(id_categoria)==1:
				raise Excepcion("Error: No se puede eliminar la categoria por default")
			if len(cats)>=2 :
				Entradaln.setentradascatdefaultcultura(id_categoria)
			cate=Categorialn.getcategoria(id_categoria)
			cate.delete()
			#elimino la categoria
			return True
		except Exception as ex:
			raise Excepcion("Error: excepcion no controlada : "+ex.message)
		except Excepcion as ex:
			raise ex
		finally:
			pass	


	@staticmethod  
	def getcategoria(id_categoria):
		try:
			id_categoria=int(id_categoria)
			cat=Categoria.objects.get(pk=int(id_categoria))		
			return cat
		except Exception as ex:
			raise Excepcion("Error: Excepcion no controlada : "+ex.message)
		except Excepcion as ex:
			raise ex
		finally:
			pass

	@staticmethod
	def getcountcategoria(id_categoria):
		entradas=Entradaln.getentradasbycategoria(id_categoria)
		return len(entradas)
	@staticmethod
	def getcountcategoriacultura(id_categoria):
		entradas=Entradaln.getentradasbycategoriacultura(id_categoria)
		return len(entradas)

	@staticmethod
	def getcategoriassort(count):
		ca=Categorialn.getcategorias()
		diccionario={}
		for i in ca:
			
			diccionario[i]=Categorialn.getcountcategoria(i.id_categoria)
		lsort = diccionario.items()
		lsort.sort(key=lambda x: x[1],reverse=True)
		nuevodic={}
		for i in lsort[:count]:		

			nuevodic[(i[0])]=Entradaln.getentradasbycategoria(i[0].id_categoria)[:4]
		
		
		return nuevodic
	@staticmethod
	def getcategoriassortcultura(count):
		ca=Categorialn.getcategorias()
		diccionario={}
		for i in ca:			
			diccionario[i]=Categorialn.getcountcategoriacultura(i.id_categoria)
		lsort = diccionario.items()
		lsort.sort(key=lambda x: x[1],reverse=True)
		nuevodic={}
		for i in lsort[:count]:		
			nuevodic[(i[0])]=Entradaln.getentradasbycategoriacultura(i[0].id_categoria)[:4]
		
		
		return nuevodic
class Userln(object):
	"""docstring for User"""
	def __init__(self, arg):
		super(User, self).__init__()
		self.arg = arg
	
	@staticmethod  
	def getusers():
		#Return todos los usuarios
		users=Usuario.objects.all()
		return users
	
	@staticmethod 
	def getusersactivos():
		users=Usuario.objects.filter(is_staff=True)
		return users
		
	@staticmethod  
	def getuser(id_user):
		try:
			id_user=int(id_user)
			user=Usuario.objects.get(pk=id_user)
			return user			
		except Exception as ex:
			raise Excepcion("Error: Exepcion no controlada : "+ex.message)
		except Excepcion as ex:
			raise ex
		finally:
			pass
		
	@staticmethod  
	def activaruser(id_user):
		try:
			user=getuser(id_user)
			user.is_staff=not user.is_staff
			user.save()
		except Exception as ex:
			raise Excepcion("Error: Excepcion no controlada : "+ex.message)
		except Excepcion as ex:
			raise ex
		finally:
			pass
		
	@staticmethod  
	def esactivo(id_user):
		try:
			id_user=int(id_user)
			user=self.getuser(id_user)
			return user.is_staff

		except Exception as ex:
			raise Excepcion("Error: Excepcion no controlada : "+ex.message)
		except Excepcion as ex:
			raise ex
		finally:
			pass
		
	@staticmethod  
	def existeuser(id_user):
		try:
			id_user=int(id_user)
			user=Usuario.objects.filter(pk=id_user)
			return len(user)>=1
		except Exception as ex:
			raise Excepcion("Error: Excepcion no controlada : "+ex.message)
		except Excepcion as ex:
			raise ex
		finally:
			pass

	@staticmethod 
	def existethisusername(tusername):
		try:
			username=Usuario.objects.filter(username=tusername)
			if len(username)>=1:
				return True 
			return False
		except Exception as ex:
			return False		
		finally:
			pass
		pass

	@staticmethod 
	def setrol(id_user,nuevo_rol):
		user=Userln.getuser(id_user)
		user.rol=nuevo_rol 
		user.save()



