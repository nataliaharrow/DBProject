from django.db import models

# Create your models here.
# Schools (schoolId, schoolName, schoolAddress, schoolType)
class School(models.Model):
    school_name = models.CharField(max_length=30)
    school_address = models.CharField(max_length=200)

# Majors (majorId, majorName)
class Major(models.Model):
    major_name = models.CharField(max_length=30)
