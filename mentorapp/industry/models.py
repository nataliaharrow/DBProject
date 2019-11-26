from django.db import models


# Create your models here.
# Industries (industryId, industryName)
class Industry(models.Model):
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
        (INDUSTRY, 'Industry'),
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
