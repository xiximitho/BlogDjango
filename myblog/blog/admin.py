from django.contrib import admin
from .models import Post

#Registrando no painel de administrador o conjunto POST, assim podendo editar pelo painel de ADM.
# Usando uma lista personalizada para mostrar.  (PODE SER USADO O COMUM TAMBEM admin.site.register(Post) )

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body') #definindo campos de pesquisa no admin
    prepopulated_fields = {'slug': ('title',)} #dizendo que ao criar um post, o campo slug será pre populado com o Titulo do post
    raw_id_fields = ('author',) #utilizado para pesquisar um usuário (util quando há varios usuários em um sistema.
    date_hierarchy = 'publish'  #define a hierarquia da lista utilizando data, assim organizando melhor.
    ordering = ('status', 'publish') #opcao de ordenacao por status e publicacao