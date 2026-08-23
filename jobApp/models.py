from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserModel(AbstractUser):
    USER_TYPE = [
        ('JobSeeker','JobSeeker'),
        ('Recruiters','Recruiters')
    ]

    user_types = models.CharField(choices=USER_TYPE,max_length=20, null=True)

