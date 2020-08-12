# -*- coding: utf-8 -*-
# @Time    : 2020-08-02 7:57
# @Author  : liudongyang
# @FileName: urls.py.py
# @Software: PyCharm

from django.urls import path, include
from sign import views

urlpatterns = [
    path('', views.index),


]