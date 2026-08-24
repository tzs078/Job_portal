from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserModel(AbstractUser):
    USER_TYPE = [
        ('JobSeeker','JobSeeker'),
        ('Recruiters','Recruiters')
    ]

    user_types = models.CharField(choices=USER_TYPE,max_length=20, null=True)

    def __str__(self):
        return self.username
    

class RecProfile(models.Model):
    user = models.OneToOneField(UserModel,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100,null=True)
    company_description = models.TextField(null=True)
    company_location = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.company_name

class JobSeekerProfile(models.Model):
    user = models.OneToOneField(UserModel,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    skill = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name


    
    
    
