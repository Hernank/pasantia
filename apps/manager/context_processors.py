from apps.LN.ln import *
def ejemplo(request):
	return  {'hola':'hernan maza Salinas'}

def miscategorias(request):
	allcategorias=Categorialn.getcategorias()
	milista=[]
	for i in allcategorias:
		count=Categorialn.getcountcategoria(i.id_categoria)
		milista.append({'categoria':i,'len':count})	

	
	milista.sort( key=lambda milen: milen['len'],reverse=True)  
	return {'ctxcategorias':milista}


def misentradas(request):
	ent=Entradaln.ultimasentradas(4)
	return {'lastentradas':ent,}

def userpersonalizado(request):
	
	if Admin.estaLogueado(request.user):
		user= Usuario.objects.get(pk=request.user.id)
		return {'userpersonalizado':user,}
	return {'userpersonalizado':"user",}