from django.contrib import admin
from .models import Post, Evento
from django.contrib.auth.models import User
# Register your models here.

#Registrando no painel de administrador o conjunto POST, assim podendo editar pelo painel de ADM.
# Usando uma lista personalizada para mostrar.  (PODE SER USADO O COMUM TAMBEM admin.site.register(Post) )
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish','status')
    search_fields = ('title','author','publish','status') #definindo campos de pesquisa no admin
    prepopulated_fields = {'slug':('title',)} #dizendo que ao criar um post, o campo slug será pre populado com o Titulo do post
    raw_id_fields = ('author',) #utilizado para pesquisar um usuário (util quando há varios usuários em um sistema.
    date_hierarchy = 'publish' #define a hierarquia da lista utilizando data, assim organizando melhor.
    ordering = ('status', 'publish') #opcao de ordenacao por status e publicacao

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('title','event_date', 'status')
    search_fields = ('title','event_date', 'status')
    ordering = ('status', 'event_date')  # opcao de ordenacao por status e publicacao