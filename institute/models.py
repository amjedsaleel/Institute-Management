from django.db import models
from django.core.validators import ValidationError

# Local django
from accounts.models import User

# Create your models here.


class Institute(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True, help_text='Full name of college')
    short_name = models.CharField(max_length=15, unique=True, help_text='Short name of college. Spaces are not allowed')
    website = models.URLField(blank=True)
    phone_no = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name

