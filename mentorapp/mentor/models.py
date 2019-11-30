from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# Mentors (userId, schoolId, industryId, position)
class Mentor(models.Model):
    user = models.OneToOneField('app_user.User', on_delete=models.CASCADE)

    # school = models.ForeignKey(
    #     'school.School',
    #     on_delete=models.CASCADE,
    #     blank=True,)
    #
    # company = models.ForeignKey(
    #     'company.Company',
    #     on_delete=models.CASCADE,
    #     blank=True,
    #     default='company',
    # )

    position = models.CharField(max_length=40)

