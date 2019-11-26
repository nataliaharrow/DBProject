from django.db import models

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
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email_address = models.CharField(max_length=50)
    bio = models.CharField(max_length=1000, default='bio')
    user_type = models.ForeignKey(
        'UserType',
        on_delete=models.CASCADE,
        blank=True,)
    # many to one: Profile points to many users, but each user has only one profile
    profile = models.ForeignKey(
        'user_profile.UserProfile',
        on_delete=models.CASCADE,
        blank=True,
        default='profile',
    )
