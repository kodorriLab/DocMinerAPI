from django.db import models

class Addresses(models.Model):
    name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    created = models.DateTimeField(auto_created=True)

    class Meta:
        ordering = ['created']

# Create your models here.
