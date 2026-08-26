from django.contrib import admin
from jobApp.models import *
# Register your models here.

admin.site.register([UserModel,RecProfile,JobSeekerProfile,JobPostModel,JobApplyModel])
