from django.conf import settings
from django.db import models
from django.utils import timezone

class Articol(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titlu = models.CharField(max_length=200)
    text = models.TextField()
    data_creatie = models.DateTimeField(default=timezone.now)
    data_publicatie = models.DateTimeField(blank=True, null=True)

    def publica(self):
        self.data_publicatie = timezone.now()
        self.save()

    def __str__(self):
        return self.titlu    
