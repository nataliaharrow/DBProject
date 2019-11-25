from django.db import models
from industry.models import Industry
from school.models import School
from user.models import User

# Create your models here.
# Mentors (userId, schoolId, industryId, position)
class Mentor(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=40)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)