from django.db import models
from django.core.validators import ValidationError

# Local django
from accounts.models import User

# Create your models here.


class Institute(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True, help_text='eg:- Kozhikode Institute')
    short_name = models.CharField(max_length=15, unique=True, help_text='eg:- KI')
    website = models.URLField(help_text='eg:- kozhikodeinstitute.com', blank=True,)
    phone_no = models.CharField(max_length=15, help_text='eg:- 0495 2211545', blank=True)
    address = models.TextField(max_length=255, help_text='Provide address of the institute', blank=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, blank=True)
    department_name = models.CharField(max_length=30, verbose_name='Department Name: ')

    class Meta:
        unique_together = ('institute', 'department_name',)

    def __str__(self):
        return self.department_name
