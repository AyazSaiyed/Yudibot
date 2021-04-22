from django.db import models
import uuid
# Create your models here.
from django.utils.timezone import now

    

class ClientEnquiries(models.Model):
	uid = models.UUIDField(primary_key = True, default = uuid.uuid4)
	date = models.DateTimeField(default=now)
	username = models.TextField(default='', max_length=100)
	enquriy = models.TextField(default='', max_length=100)
	email = models.EmailField()
	phone = models.TextField()

	def __str__(self):
		return self.username



class JobApplicants(models.Model):
	uid = models.UUIDField(primary_key = True, default = uuid.uuid4)
	date = models.DateTimeField(default=now)
	candidatename = models.TextField(default='', max_length=100)
	appliedfor = models.TextField(default='', max_length=100)
	email = models.EmailField()
	experience = models.TextField(default='')
	resumeurl = models.TextField(default='')

	def __str__(self):
		return self.appliedfor

