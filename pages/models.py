from django.db import models
from datetime import datetime

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    livro = models.CharField(max_length=200)
    autor_livro = models.CharField(max_length=200)
    data = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    conteudo = models.TextField()

    def __str__(self):
        return self.titulo
