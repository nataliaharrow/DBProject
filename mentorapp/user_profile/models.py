from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField('app_user.User', on_delete=models.CASCADE, null=True)

    image = models.ImageField(default='default.jpg', upload_to='user_profile_pictures', null=True)

    def __str__(self):
        return f'{self.user.username}UserProfile '


