from django.db import models
from django.utils import timezone


# Create your models here.
class RangerTypes(models.Model):
    RANGER_TYPE_CHOICE = [
        ('RED', 'RED RANGER'),
        ('YLW', 'YELLOW RANGER'),
        ('PNK', 'PINK RANGER'),
        ('BLU', 'BLUE RANGER'),
        ('GRN', 'GREEN RANGER'),
        ('GLD', 'GOLDEN RANGER'),
    ]

    name = models.CharField(max_length=80)
    image = models.ImageField(upload_to='Rangers/')
    date_added = models.DateTimeField(default=timezone.now)

    type = models.CharField(max_length=3, choices = RANGER_TYPE_CHOICE)


    
