# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Topic(models.Model):
    """博客主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def _unicode__(self):
        '''显示模型的简单表示，此处返回text属性的字符串表示'''
        return self.text