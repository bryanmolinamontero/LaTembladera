from django.contrib import admin
from django.db import models

# Create your models here.

class Noticias(models.Model):
    titulo=models.CharField(max_length=200,help_text='Ingrese el titulo de la noticia...')
    fecha=models.DateField(auto_now=True)
    imagen=models.ImageField(upload_to='noticias',help_text='Seleccione la imagen para la noticia...', null=True,blank=True)
    contenido=models.TextField(help_text='Escribir el contenido de la nueva noticia...')
    #contenido = tinymce_models.HTMLField()

    class Meta:
        verbose_name_plural = "Noticias"

    def __unicode__(self):
        return "%s , %s , %s, %s"%(self.id,self.titulo, self.imagen,self.contenido)


class NoticiasAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'contenido')
    search_fields = ('fecha',)
admin.site.register(Noticias, NoticiasAdmin)