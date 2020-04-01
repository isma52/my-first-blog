# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 14:22:46 2020

@author: iamor
"""

from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)