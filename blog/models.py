from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    text = models.TextField()
    creacion_fecha = models.DateTimeField(default=timezone.now)
    publicacion_fecha = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.publicacion_fecha = timezone.now()
        self.save
    
    def __str__(self):
        return self.titulo