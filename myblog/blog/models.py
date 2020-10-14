from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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


    class Meta:
        ordering = ('-publish',) #serao ordeenados pela data de publicacao

    def __str__(self):
        return self.title