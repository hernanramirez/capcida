from django.db import models
from ..users.models import User


class ModelBorrar(models.Model):
    demo = models.CharField(max_length=100)

    def __str__(self):
        return self.demo
