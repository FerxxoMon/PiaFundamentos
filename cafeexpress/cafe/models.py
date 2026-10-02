from django.db import models
class Noticia(models.Model):
    titulo=models.CharField(max_length=150)
    resumen=models.TextField()
    contenido=models.TextField()
    fecha=models.DateTimeField(auto_now_add=True)
    imagen=models.URLField(blank=True)
    def __str__(self): return self.titulo
class MensajeContacto(models.Model):
    nombre=models.CharField(max_length=100)
    correo=models.EmailField()
    asunto=models.CharField(max_length=150)
    mensaje=models.TextField()
    fecha=models.DateTimeField(auto_now_add=True)
    def __str__(self): return f'{self.nombre} - {self.asunto}'
