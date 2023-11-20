from django.db import models
from datetime import datetime
from django.conf import settings
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    livro = models.CharField(max_length=200)
    autor_livro = models.CharField(max_length=200)
    data = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    conteudo = models.TextField()

    def __str__(self):
        return self.titulo

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    data = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    texto = models.TextField()

    def __str__(self):
        return self.titulo
