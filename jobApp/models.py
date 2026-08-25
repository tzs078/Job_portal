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
    user = models.OneToOneField(UserModel,on_delete=models.CASCADE,null=True)
    company_name = models.CharField(max_length=100,null=True)
    company_description = models.TextField(null=True)
    company_location = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.company_name

class JobSeekerProfile(models.Model):
    user = models.OneToOneField(UserModel,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    skill = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name


class JobPostModel(models.Model):
    Recruiters = models.ForeignKey(UserModel,on_delete=models.CASCADE,null=True)
    JobTitle = models.CharField(max_length=100,null=True)
    NumberOfOpening = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=100,null=True)
    skill = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.JobTitle


class JobApplyModel(models.Model):
    JobSeeker = models.ForeignKey(UserModel,on_delete=models.CASCADE,null=True)
    Job = models.ForeignKey(JobPostModel, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')


    







    
    
    
