from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Post(models.Model): #tipos de status de cada Post no blog
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='blog_posts') #Um post ficará atrelado a um autor, e se o mesmo for removido, sera em Cascata no banco de dados.
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    objects = models.Manager() # #Gerenciador de modelo Default
    published = PublishedManager() #  #Gerenciador personalizado que retorna os posts publicados.

    class Meta:
        ordering = ('-publish',) #serao ordeenados pela data de publicacao

    def __str__(self):  ##Funcao para retornaro nome do Evento a cada objeto evento criado
        return self.title

    def get_absolute_url(self):    #ligar postagens especificas.
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day, self.slug])