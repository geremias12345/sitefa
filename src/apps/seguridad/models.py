from django.db import models
from django.contrib.auth.models import User
from apps.profesorado.models import Profesorado

class Perfil(models.Model):
    ROLES = [
        ('bedel', 'Bedel'),
        ('secretaria', 'Secretaría'),
        ('directivo', 'Directivo'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    rol = models.CharField(max_length=20, choices=ROLES, default='directivo')
    profesorado = models.ForeignKey(
        Profesorado,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='perfiles'
    )

    def __str__(self):
        return f"{self.user.username} ({self.get_rol_display()})"