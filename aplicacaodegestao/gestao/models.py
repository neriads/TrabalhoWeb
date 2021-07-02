from django.conf import settings
from django.db import models
from django.utils import timezone


class Empresa(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    endereco = models.TextField()
    categoria = models.TextField()
    telefone = models.TextField()
    email = models.TextField()

    def __str__(self):
        return self.nome