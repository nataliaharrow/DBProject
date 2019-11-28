from django.db import models

# Create your models here.
# Students (userId, schoolId, majorId)
class Student(models.Model):
    user = models.OneToOneField(
        'user.User',
        on_delete=models.CASCADE,
        primary_key=True,
        default='student',
    )

    school = models.ForeignKey(
        'school.School',
        on_delete=models.CASCADE,
        blank=True,)

    major = models.ForeignKey(
        'school.Major',
        on_delete=models.CASCADE,
        blank=True,)



