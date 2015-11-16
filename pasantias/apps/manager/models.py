from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Categoria(models.Model):
    # TODO: Define fields here
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField( max_length=50)
    tag = models.CharField(max_length=50,default='BLU')

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __unicode__(self):
        return self.nombre	


    # TODO: Define custom methods here
class Usuario(User):
    rol = models.CharField(max_length=50,blank=True,null=True, default='User')
    imagenperfil = models.ImageField(blank=True,upload_to=' imageperfil_users',null=True)
    linkperfil = models.CharField(blank=True,null=True, max_length=200)

class Entrada(models.Model):
    # TODO: Define fields here
    id_entrada = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150)
    imagen_libro = models.ImageField(upload_to='images_books')
    resumen = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now=True)    
    libro = models.FileField(upload_to='file_books',blank=True,null=True)    
    librourl = models.URLField(blank=True,null=True)
    autor = models.ForeignKey(User)
    categoria = models.ForeignKey(Categoria)
    tag = models.CharField(max_length=50,default='BLU')
    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"

    def __unicode__(self):
        return self.titulo

class Noticia(models.Model):
    id_noticia = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150)
    imagen_noticia = models.ImageField(blank=True,upload_to='news')
    contenido = models.TextField()
    autor = models.ForeignKey(Usuario)
    fecha_publicacion = models.DateTimeField(auto_now=True)
    tag = models.CharField(max_length=50,default="BLU")
    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"

    def __unicode__(self):
        return self.titulo
    


class UserProfile(models.Model):
    GENDERS = ( ('male', 'Male'),('female', 'Female'))
    user = models.OneToOneField(User, unique=True)
    gender = models.CharField(max_length=20, null=True, blank=True, choices=GENDERS)
    city = models.CharField(max_length=250, null=True, blank=True)
    dob = models.DateField(blank=True, null=True)
    locale = models.CharField(max_length=10, blank=True, null=True)
    def __unicode__(self):
        return u'%s profile' % self.user.username




class FacebookStatus(models.Model):
    class Meta:
        verbose_name_plural = 'Facebook Statuses'
        ordering = ['publish_timestamp']
    STATUS = (
            ('draft', 'Draft'),
            ('approved', 'Approved'),
            )
    status = models.CharField(max_length=255, 
    choices=STATUS, default=STATUS[0][0])
    publish_timestamp = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User)
    message = models.TextField(max_length=255)
    link = models.CharField(null=True, blank=True,max_length=200)

    def __unicode__(self):
        return self.message









