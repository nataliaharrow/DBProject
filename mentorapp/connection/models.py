from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Connection(models.Model):
    STATUS_TYPES = [
        (0, 'Pending'),
        (1, 'Accepted'),
        (2, 'Declined'),
    ]

    user_one = models.ForeignKey(
        'user.User',
        related_name='user_one',
        on_delete=models.CASCADE,
        db_column='user_one',
    )

    user_two = models.ForeignKey(
        'user.User',
        related_name='user_two',
        on_delete=models.CASCADE,
        db_column='user_two',
    )

    status = models.PositiveIntegerField(
        validators = [MaxValueValidator(2)],
        choices=STATUS_TYPES,
        default=0,
        db_column='status')

    action_user = models.ForeignKey(
        'user.User',
        related_name='action_user',
        on_delete=models.CASCADE,
        db_column='action_user',
    )