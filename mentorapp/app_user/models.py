from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# Create your models here.
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
    industries = models.ManyToManyField(Industry)
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

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_mentor = models.BooleanField(default=False)
    requests = models.ManyToManyField(Request)
    schools = models.ManyToManyField(School)
    majors = models.ManyToManyField(Major)
    companies = models.ManyToManyField(Company)
    industries = models.ManyToManyField(Industry)

class Mentor(models.Model):
    user = models.OneToOneField('app_user.User', on_delete=models.CASCADE)


class Student(models.Model):
    user = models.OneToOneField('app_user.User', on_delete=models.CASCADE)



