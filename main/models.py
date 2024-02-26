from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    cuerpo = models.TextField(help_text="Incluye el contenido de tu articulo")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.titulo} - {self.user}'

    class Meta:
        verbose_name_plural = "Posts"



class Valoracion(models.Model):
    RATE_CHOICES = [
        (1,1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]
    rating = models.PositiveIntegerField(choices=RATE_CHOICES)
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} - {self.post.titulo} - {self.user}'

    class Meta:
        verbose_name_plural = "Valoraciones"
