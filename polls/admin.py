# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from polls.models import *
from django.contrib.admin import AdminSite
import psycopg2
from mapwidgets.widgets import GooglePointFieldWidget
from django.contrib.gis.db import models

@admin.register(Question)
class Question(admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }
    #pass

# Register your models here.
