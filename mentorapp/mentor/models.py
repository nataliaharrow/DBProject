from django.db import models
# from industry.models import Industry
# from school.models import School
# from user.models import User

# Create your models here.
# Mentors (userId, schoolId, industryId, position)
class Mentor(models.Model):
    # user_id = models.ForeignKey(
    #     'user.User',
    #     on_delete=models.CASCADE,
    #     blank=True,)

    school = models.ForeignKey(
        'school.School',
        on_delete=models.CASCADE,
        blank=True,)

    company = models.ForeignKey(
        'company.Company',
        on_delete=models.CASCADE,
        blank=True,
        default='company',
    )

    position = models.CharField(max_length=40)



