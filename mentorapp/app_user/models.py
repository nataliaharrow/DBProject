from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
# to import from this:
# from app_user.models import *
#  User, Profile, School, Major, Company, Industry, Request, UserSchool, UserMajor, UserCompany, UserIndustry, UserRequest, Connection, CompanyIndustry
from django.db import models


class Industry(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'


class Company(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'


class Request(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'


class School(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'


class Major(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_mentor = models.BooleanField(default=False)
    requests = models.ManyToManyField(Request, null=True)
    schools = models.ManyToManyField(School, null=True)
    majors = models.ManyToManyField(Major, null=True)
    companies = models.ManyToManyField(Company, null=True)
    industries = models.ManyToManyField(Industry, null=True)
    position = models.CharField(max_length=20, null=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(
        default='',
        null=True,
        blank=True,
    )
    website = models.URLField(blank=True, null=True)
    image = models.ImageField(default='default.jpg', upload_to='media', null=True)



class UserRequest(Request):
    mentor = models.ForeignKey(
        User,
        limit_choices_to={'is_mentor':True},
        on_delete=models.SET_NULL,
        null=True,
        default=None,
        related_name='mentor_request'
    )
    student = models.ForeignKey(
        User,
        limit_choices_to={'is_student':True},
        on_delete=models.CASCADE,
        null=True,
        default=None,
        related_name='student_request'
    )
    
    requesting = models.CharField(max_length = 100, default='')
    description = models.TextField( default='', null=True, blank=True)
    document = models.FileField(upload_to='requests/documents/', null=True, blank=True)


class Connection(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('C', 'Connected'),
    ]

    REQUEST_FROM_CHOICES = [
        ('S', 'Student'),
        ('M', 'Mentor'),
    ]

    mentor = models.ForeignKey(
        User,
        limit_choices_to={'is_mentor':True},
        on_delete=models.CASCADE,
        related_name='mentor_connection'
    )

    student = models.ForeignKey(
        User,
        limit_choices_to={'is_student':True},
        on_delete=models.CASCADE,
        related_name='student_connection'
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='P'
    )

    request_from = models.CharField(
        max_length=1,
        choices=REQUEST_FROM_CHOICES,
        default=None,
        null=True
    )
