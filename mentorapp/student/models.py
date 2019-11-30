from django.db import models

# Create your models here.
# Students (userId, schoolId, majorId)
class Student(models.Model):
    user = models.OneToOneField('app_user.User', on_delete=models.CASCADE)

    school = models.ManyToManyField(
        'school.School',
        blank=True, )

    major = models.ManyToManyField(
        'school.Major',
        blank=True, )
