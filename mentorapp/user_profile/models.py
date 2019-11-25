from django.db import models

# Create your models here.
class UserProfile(models.Model):
    photo = models.ImageField(height_field=20, width_field=20)