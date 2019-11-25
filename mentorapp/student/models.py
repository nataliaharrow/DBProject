from django.db import models
from school.models import School, Major

# Create your models here.
# Students (userId, schoolId, majorId)
class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)

