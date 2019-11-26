from django.db import models

# Create your models here.
# Schools (schoolId, schoolName, schoolAddress, schoolType)
class School(models.Model):
    school_name = models.CharField(max_length=30)
    school_address = models.CharField(max_length=200)

# Majors (majorId, majorName)
class Major(models.Model):
    ART = 'AR'
    BUSINESS = 'BI'
    CIVIL_ENGINEERING = 'CE'
    COMPUTER_SCIENCE = 'CS'
    FILM = 'FI'
    FINANCE = 'FN'
    HISTORY = 'HI'
    MATH = 'MT'
    MUSIC = 'MU'

    MAJOR_CHOICES = [
        (ART, 'Art'),
        (BUSINESS, 'Business'),
        (CIVIL_ENGINEERING, 'Civil Engineering'),
        (COMPUTER_SCIENCE, 'Computer Science'),
        (FILM, 'Film'),
        (FINANCE, 'Finance'),
        (HISTORY, 'History'),
        (MATH, 'Math'),
        (MUSIC, 'Music'),
    ]

    major_name = models.CharField(
        max_length=2,
        choices=MAJOR_CHOICES,
    )
