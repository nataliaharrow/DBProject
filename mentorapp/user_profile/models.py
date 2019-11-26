from django.db import models

# Create your models here.
class UserProfile(models.Model):
    # photo = models.ImageField(height_field=20, width_field=20) -- gives an error so for now replaced with string
    # photo = models.CharField(max_length=12, default='')
    user = models.OneToOneField(
        'user.User',
        on_delete=models.CASCADE, #if the user is deleted - delete profile
        default='');

    def __str__(self):
        return {self.user.username}