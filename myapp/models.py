from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime  
from django.conf import settings
from django.forms.widgets import RadioSelect

class User(AbstractUser):
    is_webuser = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)


class WebUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
        
    def __str__(self):
        return self.user.username


class CompanyType(models.Model):
    names = models.CharField(max_length=200)

    def __str__(self):
        return self.names


class AvailablePosts(models.Model):
    companytype = models.ForeignKey(CompanyType, on_delete=models.CASCADE)
    names = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.companytype} - {self.names} "



class EmployerDetails(models.Model): 

  #  id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    username = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, related_name='company_name')
    company_name = models.CharField(max_length = 200) 
    email = models.EmailField(blank=True)
    about_us = models.TextField()
    companytype = models.ForeignKey(CompanyType, on_delete=models.SET_NULL, null=True)
    availableposts = models.ForeignKey(AvailablePosts, on_delete=models.SET_NULL, null=True)
    strength = models.IntegerField()
    vacancies = models.IntegerField()
    last_modified = models.DateTimeField(auto_now_add = True) 
    our_requirements = models.TextField(null=True)
    our_offical_website = models.URLField(max_length=200, null=True)
    created = models.DateTimeField(default=datetime.now(), editable=False)
    updated = models.DateTimeField(default=datetime.now(), editable=False)

#    img = models.ImageField(upload_to = "images/") 
   
       
    def __str__(self): 
        return f"{self.company_name} "

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'posted_by', None) is None:
            obj.posted_by = request.user.username
        obj.save()


class ApplicationData(models.Model):
    employer_name = models.CharField(max_length=255, blank=True)
  
    def __str__(self):
        return f"{self.employer_name} "


FRESHER_CHOICES = [
    ('yes', 'YES'),
    ('no', 'NO'),
   
    ]

class Application(models.Model): 

    username = models.CharField(max_length = 200, null=True) 
    first_name = models.CharField(max_length = 200, null=True) 
    last_name = models.CharField(max_length = 200, null=True) 
    email = models.EmailField(blank=True)
    company_name = models.ForeignKey(EmployerDetails,on_delete=models.SET_NULL,null=True, max_length = 200) 
    describe_yourself = models.TextField()
    resume = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(default=datetime.now(), editable=False)
    fresher = models.CharField(max_length=11,choices=FRESHER_CHOICES, null=True)
    companytype = models.ForeignKey(CompanyType, on_delete=models.SET_NULL, null=True)
   
   
    def __str__(self):
        return f"{self.company_name} "



class Ratings(models.Model):
     RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
     displayname = models.CharField(max_length = 200, null=True)    
     email = models.EmailField(blank=True)
   #  company_name = models.ForeignKey(EmployerDetails,on_delete=models.SET_NULL,null=True, max_length = 200) 
     company_name = models.CharField(max_length = 200, null=True) 
     rating = models.IntegerField(choices=RATING_CHOICES,null=True)
     review = models.TextField(null=True)
     published_at = models.DateTimeField(default=datetime.now(), editable=False)

