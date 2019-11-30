from django.db import models

# Create your models here.
class MentorProfile(models.Model):
    mentor = models.ForeignKey(
        'mentor.Mentor',
        on_delete=models.CASCADE,
    )

    bio = models.CharField(
        max_length=300,
        default='bio',
    )

    school = models.ForeignKey(
        'school.School',
        on_delete=models.CASCADE,
        blank=True,)

    major = models.ForeignKey(
        'school.Major',
        on_delete=models.CASCADE,
        blank=True,)

    company = models.ForeignKey(
        'company.Company',
        on_delete=models.CASCADE,
        blank=True,
    )