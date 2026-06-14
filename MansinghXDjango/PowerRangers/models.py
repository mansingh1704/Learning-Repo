from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class RangerTypes(models.Model):
    RANGER_TYPE_CHOICE = [
        ('RED', 'RED RANGER'),
        ('YLW', 'YELLOW RANGER'),
        ('PNK', 'PINK RANGER'),
        ('BLU', 'BLUE RANGER'),
        ('GRN', 'GREEN RANGER'),
        ('GLD', 'GOLDEN RANGER'),
        ('BLK', 'BLACK RANGER'),
    ]

    name = models.CharField(max_length=80)
    image = models.ImageField(upload_to='Rangers/')
    date_added = models.DateTimeField(default=timezone.now)

    type = models.CharField(max_length=3, choices = RANGER_TYPE_CHOICE)

    def __str__(self):
        return self.name #to inject in admin


# One to Many   (like for one ranger there can be many reviews)

class RangerReview(models.Model):
    ran_ger=models.ForeignKey(RangerTypes, on_delete=models.CASCADE, related_name='reviews')
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    rating_point = models.IntegerField()
    comment = models.CharField(max_length=500)
    date_added_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} reviewed for {self.ran_ger.name}'


# Many to Many  (like example of many stores be selling many power rangers)

class RangerStores(models.Model):
    storeName=models.CharField(max_length = 50)
    storeLocated = models.TextField()
    ranger_type = models.ManyToManyField(RangerTypes,related_name= "Location_of_Store")   # how many variety are available at particular location
   
    def __str__(self):
        return self.name
    

# One to One (suppose the special ability of each ranger is unique do its a one to one relation)

class RangerAbility(models.Model):
    ranger_ability = models.OneToOneField( RangerTypes, on_delete=models.CASCADE , related_name='abilities')
    abilityName = models.CharField(max_length= 100)
    abilityEffects= models.TextField()

    def __str__(self):
        return f'Special Ability of {self.abilityName}'
