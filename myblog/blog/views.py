from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.published.all() #Realizando a chamada da funcao feita no Models.py para a View
    return render(request, 'blog/post/list.html',{'posts': posts}) #FUNCAO RENDER PARA PLOTAR A VIEW, recebe como parametro request, path do template e variaveis do contexto para renderizar

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish_year=year,
                             publish_month=month,
                             publish_day=day) #SE o objeto existir ele retorna ao objeto post, caso contrario exibe 404

    return render(request, 'blog/post/detail.html', {'post': post})

