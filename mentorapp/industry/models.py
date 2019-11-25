from django.db import models

# Create your models here.
# Industries (industryId, industryName)
class Industry(models.Model):
    industry_name = models.CharField(max_length=30)