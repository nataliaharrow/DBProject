from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
# to import from this:
# from app_user.models import User, UserProfile, School, Major, Company, Industry, Request, UserSchool, UserMajor, UserCompany, UserIndustry, UserRequest, Connection, CompanyIndustry
from django.db import models


class Industry(models.Model):

    industry_type_name = models.CharField(
        max_length=25,
    )

    def __str__(self):
        return f'{self.industry_type_name}'


class Company(models.Model):
    company_name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.company_name}'


class Request(models.Model):

    request_type_name = models.CharField(
        max_length=20,
    )

    def __str__(self):
        return f'{self.request_type_name}'


class School(models.Model):

    school_name = models.CharField(max_length=30)
    school_address = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.school_name}'


class Major(models.Model):

    major_name = models.CharField(
        max_length=30,
    )

    def __str__(self):
        return f'{self.major_name}'


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_mentor = models.BooleanField(default=False)
    requests = models.ManyToManyField(Request)
    schools = models.ManyToManyField(School)
    majors = models.ManyToManyField(Major)
    companies = models.ManyToManyField(Company)
    industries = models.ManyToManyField(Industry)
    position = models.CharField(max_length=20, null=True)


class UserProfile(models.Model):
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
        on_delete=models.CASCADE,
        related_name='mentor_request'
    )
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='student_request'
    )


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
        choices=STATUS_CHOICES,
        default=None,
        null=True
    )



# class UserSchool(School):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#
#
# class UserMajor(Major):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#
#
# class UserCompany(Company):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#
#
# class UserIndustry(Industry):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

# class CompanyIndustry(Industry):
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
