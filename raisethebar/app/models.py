from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel
from model_utils import Choices

# Create your models here.

class Firm(models.Model):
	firm_name = models.CharField(max_length=100)

	def __str__(self):
		return self.firm_name

class Contact(TimeStampedModel):
	first_name = models.CharField(max_length=50) 
	last_name = models.CharField(max_length=50)
	email = models.EmailField(blank=True, null=True)
	phone_number = models.CharField(max_length=20)
	firm = models.ForeignKey(Firm)

	def __str__(self):
		return self.last_name + "," + self.first_name

class Note(TimeStampedModel):
	user = models.ForeignKey(User)
	contact = models.ForeignKey(Contact, blank=True, null=True)
	firm = models.ForeignKey(Firm)
	content = models.TextField()

	def __str__(self):
		return self.id

class Reminder(TimeStampedModel):
	note = models.ForeignKey(Note)
	reminder = models.DateTimeField()
	content = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.id