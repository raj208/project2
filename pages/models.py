from distutils.command.upload import upload
from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
class Team(models.Model):
    first_name = models.CharField (max_length=255)
    last_name = models.CharField (max_length=255)
    designation  = models.CharField (max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',blank = True)
    facebook_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    linkedin_link = models.URLField(max_length=100)
    instagram_link = models.URLField(max_length=100)
    github_link = models.URLField(max_length=100, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name
    
    # def imageURL(self):
    #     if self.photo:
    #         return self.photo.url
    #     else:
    #         return 'images/placeholder.png'
    # @property
    # def imageURL(self):
    #     try:
    #         url = self.photo.url
    #     except:
    #         url=''
    #     return url
