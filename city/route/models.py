from __future__ import unicode_literals

from django.db import models

from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

class Source(models.Model):
    source_text = models.CharField(max_length=200)
#    pub_date = models.DateTimeField('date published')
    id_order = models.IntegerField(default=0)
    def __str__(self):
        return self.source_text    

class Destination(models.Model):
#    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    destination_text = models.CharField(max_length=200)
#    times = models.IntegerField(default=0)
#    query_date = models.DateTimeField('date queried')
    id_order = models.IntegerField(default=0)
    def __str__(self):
        return self.destination_text    

class Location(models.Model):
    location_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    id_order = models.IntegerField(default=0)
    def __str__(self):
        return self.location_text    

class Name(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name_text = models.CharField(max_length=200)
    times = models.IntegerField(default=0)
    query_date = models.DateTimeField('date queried')
    id_order = models.IntegerField(default=0)
    def __str__(self):
        return self.name_text    

