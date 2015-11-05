# -*- coding: utf-8 -*-
from django.db import models

class Report(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    sd = models.CharField(max_length=200)
    ld = models.CharField(max_length=1000)
    public = models.BooleanField(default=False)
    def __str__(self):
    	return self.name;
    
class Document(models.Model):
    report = models.ForeignKey(Report, null=True)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
