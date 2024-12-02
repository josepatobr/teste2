from django.db import models

class Pessoas(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=1000, null=True)
    senha = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
