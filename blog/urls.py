# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 10:33:14 2020

@author: iamor
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]