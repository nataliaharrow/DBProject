from django.db import models

# Create your models here.
# UserTypes (userTypeId, userTypeName) (Types: Students, Mentors)
class UserType(models.Model):
    user_type_name = models.CharField(max_length=10)

# Users (userId, firstName, lastName, emailAddress, userTypeId)
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email_address = models.CharField(max_length=50)
    bio = models.CharField(max_length=1000, default='bio')
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)