from __future__ import unicode_literals
from django.contrib.gis.db import models
#from django.db.models import Manager as GeoManager
import os
#from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    geom = models.PointField(null=True, blank=True)
    #objects = models.Geomanager()
    #objects = models.Geomanager()

    def __unicode__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
