from __future__ import unicode_literals

from django.db import models

from django import forms
# Create your models here.

class Share(models.Model):
    name=models.CharField(max_length=120,blank=True,null=True)
    describ=models.CharField(max_length=120,blank=True,null=True)
    currentprice=models.DecimalField(max_digits=7,decimal_places=2,default=1000.0000)
    queries=models.PositiveSmallIntegerField(default=0)
	
    def __str__(self):
        return self.name
class News(models.Model):
    news=models.CharField(max_length=120,blank=True,null=True)
    weight=models.DecimalField(max_digits=4,decimal_places=2,default=-1)
    
    def __str__(self):
        return self.news
class Timer(models.Model):
    name=models.CharField(max_length=120,blank=True,null=True)
    time=models.PositiveSmallIntegerField(default=0)	
    def __str__(self):
        return self.name


class ShareDetail(models.Model):
	id=models.PositiveSmallIntegerField(primary_key='True')
	username=models.CharField(max_length=120,blank=True,null=True)
	Amazon=models.PositiveSmallIntegerField(default=0)
	Google=models.PositiveSmallIntegerField(default=0)
	Facebook=models.PositiveSmallIntegerField(default=0)
	share1=models.PositiveSmallIntegerField(default=0)
	share2=models.PositiveSmallIntegerField(default=0)
	share3=models.PositiveSmallIntegerField(default=0)
	share4=models.PositiveSmallIntegerField(default=0)
	share5=models.PositiveSmallIntegerField(default=0)
	share6=models.PositiveSmallIntegerField(default=0)
	share7=models.PositiveSmallIntegerField(default=0)
	share8=models.PositiveSmallIntegerField(default=0)
	share9=models.PositiveSmallIntegerField(default=0)
	share10=models.PositiveSmallIntegerField(default=0)
	share11=models.PositiveSmallIntegerField(default=0)
	share12=models.PositiveSmallIntegerField(default=0)
	share13=models.PositiveSmallIntegerField(default=0)
	share14=models.PositiveSmallIntegerField(default=0)
	share15=models.PositiveSmallIntegerField(default=0)
	share16=models.PositiveSmallIntegerField(default=0)
	share17=models.PositiveSmallIntegerField(default=0)
	share18=models.PositiveSmallIntegerField(default=0)
	share19=models.PositiveSmallIntegerField(default=0)
	share20=models.PositiveSmallIntegerField(default=0)
	def __str__(self):
		return self.username
