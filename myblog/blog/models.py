from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

#criando um gerenciador de madelo do banco
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')  #funcao que retorna os posts publicados.


class Post(models.Model):  #tipos de status de cada Post no blog
    STATUS_CHOICES = (('draft','Draft'),
                      ('published','Published'),
                      )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts') #Um post ficará atrelado a um autor, e se o mesmo for removido, sera em Cascata no banco de dados.

    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    objects = models.Manager() #Gerenciador de modelo Default
    published = PublishedManager() #Gerenciador personalizado que retorna os posts publicados.

    class Meta:
        ordering = ('-publish',) #serao ordeenados pela data de publicacao

    def __str__(self):
        return self.title

    def get_absolute_url(self): #ligar postagens especificas.
        return reverse('blog:post_detail', args=[self.publish.year,
                                                 self.publish.month,
                                                 self.publish.day,
                                                 self.slug])



class Evento(models.Model):
    STATUS_EVENTO = (('encerrado','Encerrado'),
                     ('aguardando','Aguardando'))

    status = models.CharField(max_length=15, choices=STATUS_EVENTO)
    title = models.CharField(max_length=255)
    event_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event')
    description = models.TextField()

    def __str__(self): ##Funcao para retornaro nome do Evento a cada objeto evento criado
        return self.title