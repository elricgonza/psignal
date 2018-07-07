# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from polls.models import *
from django.contrib.admin import AdminSite
import psycopg2

@admin.register(Question)
class Question(admin.ModelAdmin):
    pass

# Register your models here.
