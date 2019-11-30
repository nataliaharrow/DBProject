from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from app_user.models import User

# Create your models here.
class StudentProfile(models.Model):
    # user = models.OneToOneField('app_user.User', on_delete=models.CASCADE)

    image = models.ImageField(default='default.jpg', upload_to='student_profile_pictures')

#
# @receiver(post_save, sender=User)
# def create_user(sender, instance, created, **kwargs):
#     if created:
#         StudentProfile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user(sender, instance, **kwargs):
#     instance.studentprofile.save()

