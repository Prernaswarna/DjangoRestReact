from django.db import models
from djrichtextfield.models import RichTextField
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.


class User(AbstractUser):
    typeofuser = models.BooleanField(default=True);
    enroll = models.IntegerField(unique=True);
    acstoken = models.TextField(max_length=1000);
    
    


class Project(models.Model):
    project_name=models.CharField(max_length=200);
    wiki = RichTextField();
    project_members = models.ManyToManyField(User);
    class Meta:
        ordering=['project_name'];



class Bug(models.Model):
    heading = models.CharField(max_length=200);
    description = models.CharField(max_length=1000 , default="Not provided");
    doc=models.ImageField(upload_to='documents/',null=True , blank=True);
    tags = models.CharField(max_length=200);
    statusval = models.CharField(max_length=100);
    reporter = models.ForeignKey(User , on_delete=models.CASCADE, related_name='rep');
    project = models.ForeignKey(Project , on_delete=models.CASCADE,related_name='issues');
    assignee = models.ForeignKey(User , on_delete=models.CASCADE , related_name='assigned', default=None,null=True);
    class Meta:
        ordering=['heading'];
    def __str__(self):
        return '%s' %(self.heading)
    def get_readonly_fields(self , request , obj=None):
        if obj:
            return ["heading" , "description" , "tags"]
        else:
            return []




class Comment(models.Model):
    bug = models.ForeignKey(Bug , on_delete=models.CASCADE,related_name='comments');
    creator = models.ForeignKey(User , on_delete=models.CASCADE);
    body = models.TextField();
    created_on = models.DateTimeField(auto_now_add=True);
    class Meta:
        ordering=['created_on'];
    def __str__(self):
        return '%s' %(self.body)


