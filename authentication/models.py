# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models

# Create your models here.
from django.contrib.auth.models import User
import uuid
from django.utils.timezone import now

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	isSales = models.BooleanField(default=False)
	isAdmin = models.BooleanField(default=False)
	isHR = models.BooleanField(default=False)
	usersname = models.CharField(max_length=100)
	passwords = models.CharField(max_length=100)

	def __str__(self):
		return str(self.username)

# class UserTable(models.Model):
# 	uid = models.UUIDField(primary_key = True, default = uuid.uuid4)
# 	date = models.DateTimeField(default=now)
# 	username = models.CharField(max_length=100)
# 	password = models.CharField(max_length=100)
# 	email = models.EmailField()
# 	phone = models.CharField(max_length=100)
# 	isSales = models.BooleanField(default=False)
# 	isAdmin = models.BooleanField(default=False)
# 	isHR = models.BooleanField(default=False)


# 	def __str__(self):
# 		return self.username