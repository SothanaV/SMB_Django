# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
class Box(models.Model):
    time    = models.DateTimeField(auto_now_add=True)
    nodeid  = models.CharField(max_length=3, blank=False)
    temp    = models.FloatField(default=0.0)
    humi    = models.FloatField(default=0.0)
    class Meta:
        ordering = ['nodeid']
    
class Profile(models.Model):
    day     = models.CharField(max_length=3,blank=False,default=0.0)
    temp    = models.IntegerField(default=0.0)
    humi    = models.IntegerField(default=0.0)
    ontime  = models.IntegerField(default=0)
    lred    = models.IntegerField(default=0)
    lgreen  = models.IntegerField(default=0)
    lblue   = models.IntegerField(default=0)
    
        