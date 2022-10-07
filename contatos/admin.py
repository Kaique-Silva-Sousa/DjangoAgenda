from django.contrib import admin
from .models import Categoria, Contato

# Register your models here.
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id','nome','sobrenome','telefone','email','data_criacao','categoria','mostrar')
    list_display_links = ('nome','sobrenome','id')
    #list_filter = ('nome','sobrenome')
    list_per_page = 10
    search_fields = ('nome','sobrenome','telefone','email')
    list_editable = ('telefone','mostrar')

admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)