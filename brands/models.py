from django.db import models


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) # Adiciona a hora do registro e nunca mais é alterado
    updated_at = models.DateTimeField(auto_now=True) # Se atualizar, o created_at se mantém, porém o update muda

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name