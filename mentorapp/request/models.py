from django.db import models

# Create your models here.
class Request(models.Model):
    RESUME = 'RS'
    NETWORKING = 'NT'
    INTERVIEW = 'IN'
    ADVICE = 'AD'
    JOB_SEARCH = 'JB'
    COVER_LETTER = 'CV'
    LINKEDIN = 'LI'
    PORTFOLIO = 'PR'

    REQUEST_TYPE_CHOICES = [
        (RESUME, 'Resume'),
        (NETWORKING, 'Networking'),
        (INTERVIEW, 'Interview'),
        (ADVICE, 'AD'),
        (JOB_SEARCH, 'Job Search'),
        (COVER_LETTER, 'Cover Letter'),
        (LINKEDIN, 'LinkedIn'),
        (PORTFOLIO, 'Portfolio'),
    ]

    request_type_name = models.CharField(
        max_length=2,
        choices=REQUEST_TYPE_CHOICES,
    )
