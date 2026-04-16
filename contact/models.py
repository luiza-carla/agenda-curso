from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)

    def  __str__(self):
        return f'{self.last_name} {self.first_name}'