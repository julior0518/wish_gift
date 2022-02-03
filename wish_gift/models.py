# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class List(models.Model):
    owner = models.CharField(max_length=100)
    listItem = models.CharField(max_length=100)

    def __str__(self):
        return self.owner