from django.db import models

# Create your models here.
class Request(models.Model):
    request_type = models.CharField(max_length=30)