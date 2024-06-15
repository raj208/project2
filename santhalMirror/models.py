from django.db import models
from distutils.command.upload import upload
from ckeditor.fields import RichTextField


# Create your models here.
class Personalities(models.Model):
    sourceName = models.CharField(max_length=225,default="")
    SourcePhoto = models.ImageField(upload_to='photos/%Y/%m/%d',default="")
    personFirstName = models.CharField(max_length=225)
    personSecondName = models.CharField(max_length=225)
    personPhoto = models.ImageField(upload_to='photos/%Y/%m/%d')
    Photo1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    Photo2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    Photo3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    Photo4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    description = RichTextField(default="")
    