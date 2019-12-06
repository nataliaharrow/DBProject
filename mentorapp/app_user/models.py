from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
# to import from this:
# from app_user.models import User, UserProfile, School, Major, Company, Industry, Request, UserSchool, UserMajor, UserCompany, UserIndustry, UserRequest, Connection, CompanyIndustry

# user

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_mentor = models.BooleanField(default=False)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(
        default='',
        null=True,
        blank=True,
    )
    website = models.URLField(blank=True, null=True)
    image = models.ImageField(default='default.jpg', upload_to='media', null=True)

# nonuser

from django.db import models

class Industry(models.Model):
    DEFAULT = '--'
    INDUSTRY = 'IY'
    ACCOUNTING = 'AC'
    AIRLINES = 'AR'
    AGRICULTURE = 'AG'
    BANKING = 'BN'
    BEVERAGES = 'BV'
    EDUCATION = 'ED'
    ENGINEERING = 'EG'
    ENVIRONMENT = 'EN'
    FILM = 'FL'
    FOOD = 'FD'
    HEALTH = 'HT'
    INTERNET = 'IN'
    LAW = 'LW'
    MUSIC = 'MS'
    RADIO = 'RD'
    SPORTS = 'SP'
    TECH = 'TC'
    TELEVISION = 'TV'
    TRANSPORTATION = 'TR'

    INDUSTRY_TYPE_CHOICES = [
        (DEFAULT,'--'),
        (ACCOUNTING, 'Accounting'),
        (AIRLINES, 'Airlines'),
        (AGRICULTURE, 'Agriculture'),
        (BANKING, 'Banking'),
        (BEVERAGES, 'Beverages'),
        (EDUCATION, 'Education'),
        (ENGINEERING, 'Engineering'),
        (ENVIRONMENT, 'Environment'),
        (FILM, 'Film'),
        (FOOD, 'Food'),
        (HEALTH, 'Health'),
        (INTERNET, 'Internet'),
        (LAW, 'Law'),
        (MUSIC, 'Music'),
        (RADIO, 'Radio'),
        (SPORTS, 'Sports'),
        (TECH, 'Tech'),
        (TELEVISION, 'Television'),
        (TRANSPORTATION, 'Transportation'),
    ]

    industry_type_name = models.CharField(
        max_length=2,
        choices=INDUSTRY_TYPE_CHOICES,
        default=INDUSTRY,
    )


class Company(models.Model):
    company_name = models.CharField(max_length=30)
    company_address = models.CharField(max_length=200)


class Request(models.Model):
    RESUME = 'Resume'
    NETWORKING = 'Networking'
    INTERVIEW = 'Interview'
    ADVICE = 'Career Advice'
    JOB_SEARCH = 'Job Search'
    COVER_LETTER = 'Covder Letter'
    LINKEDIN = 'LinkedIn'
    PORTFOLIO = 'Portfolio'

    REQUEST_TYPE_CHOICES = [
        (RESUME, 'Resume'),
        (NETWORKING, 'Networking'),
        (INTERVIEW, 'Interview'),
        (ADVICE, 'Career Advice'),
        (JOB_SEARCH, 'Job Search'),
        (COVER_LETTER, 'Cover Letter'),
        (LINKEDIN, 'LinkedIn'),
        (PORTFOLIO, 'Portfolio'),
    ]

    request_type_name = models.CharField(
        max_length=20,
        choices=REQUEST_TYPE_CHOICES,
    )

    def __str__(self):
        return f'{self.request_type_name})'


class School(models.Model):
    DEFAULT = '--'
    COLUMBIA = 'CL'
    CITY_COLLEGE = 'CC'
    HARVARD = 'HR'
    YALE = 'YL'

    SCHOOL_CHOICES = [
        (DEFAULT, '--'),
        (COLUMBIA, 'Columbia University'),
        (CITY_COLLEGE, 'CUNY City College'),
        (HARVARD, 'Harvard University'),
        (YALE, 'Yale University'),
    ]
    school_name = models.CharField(max_length=30, choices=SCHOOL_CHOICES)
    school_address = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.school_name})'


# Majors (majorId, majorName)
class Major(models.Model):
    DEFAULT = '--'
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
        (DEFAULT, '--'),
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

# relation

class UserSchool(School):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class UserMajor(Major):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class UserCompany(Company):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class UserIndustry(Industry):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

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

class CompanyIndustry(Industry):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

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
