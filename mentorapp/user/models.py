from django.db import models
from django.contrib.auth.models import User as DjangoUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
# UserTypes (userTypeId, userTypeName) (Types: Students, Mentors)
class UserType(models.Model):
    MENTOR = 'MR'
    STUDENT = 'ST'

    USER_TYPE_CHOICES = [
        (MENTOR, 'Mentor'),
        (STUDENT, 'Student'),
    ]

    user_type_name = models.CharField(
        max_length=2,
        choices=USER_TYPE_CHOICES,
    )

# Users (userId, firstName, lastName, emailAddress, userTypeId)
class AppUser(models.Model):
    user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)

    # username = models.CharField(
    #     primary_key=True, #implies uniquness
    #     max_length=20,
    #     default='',
    #     db_column='username')
    #
    # first_name = models.CharField(
    #     max_length=30,
    #     db_column='first_name')
    #
    # last_name = models.CharField(
    #     max_length=40,
    #     db_column='last_name')
    #
    # email_address = models.CharField(
    #     unique=True,
    #     max_length=50,
    #     db_column='email')

    bio = models.CharField(
        max_length=1000,
        default='bio',
        db_column='bio')

    is_student = models.BooleanField(
        default=False,
        db_column="is_student",
    )

    is_mentor = models.BooleanField(
        default=False,
        db_column="is_mentor",
    )
    # user_type = models.ForeignKey(
    #     'UserType',
    #     on_delete=models.CASCADE,
    #     blank=True,)
    # many to one: Profile points to many users, but each user has only one profile
    # profile = models.ForeignKey(
    #     'user_profile.UserProfile',
    #     on_delete=models.CASCADE,
    #     blank=True,
    #     default='profile',
    # )

@receiver(post_save, sender=DjangoUser)
def create_user(sender, instance, created, **kwargs):
    if created:
        AppUser.objects.create(user=instance)

@receiver(post_save, sender=DjangoUser)
def save_user(sender, instance, **kwargs):
    instance.appuser.save()

