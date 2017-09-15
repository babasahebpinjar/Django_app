# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class windowsApp(models.Model):
    appName = models.CharField(max_length = 250)
    username = models.CharField(max_length = 250)
    password = models.CharField(max_length = 250)

    def __str__(self):
        return self.appName + "--" + self.username
