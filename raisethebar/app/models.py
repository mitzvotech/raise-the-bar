from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel
from model_utils import Choices

# Create your models here.

class Firm(models.Model):
	firm_name = models.CharField(max_length=100)
	status = models.BooleanField(default=False)
	headquarters = models.CharField(max_length=100, default="DC")

	def __str__(self):
		return self.firm_name

	def get_absolute_url(self):
		return "/firm/" + str(self.id)

class Contact(TimeStampedModel):
	first_name = models.CharField(max_length=50) 
	last_name = models.CharField(max_length=50)
	title = models.CharField(max_length=50, null=True, blank=True)
	email = models.EmailField(blank=True, null=True)
	phone_number = models.CharField(max_length=20, blank=True, null=True)
	contact_notes = models.TextField(blank=True, null=True)
	firm = models.ForeignKey(Firm)

	def __str__(self):
		return self.last_name + ", " + self.first_name

	def get_absolute_url(self):
		return "/contact/" + str(self.id)


class Note(TimeStampedModel):
	user = models.ForeignKey(User)
	contact = models.ForeignKey(Contact, blank=True, null=True)
	firm = models.ForeignKey(Firm)
	content = models.TextField()

	def get_absolute_url(self):
		return "/note/" + str(self.id)


	def __str__(self):
		return str(self.id)

class Reminder(TimeStampedModel):
	note = models.ForeignKey(Note)
	reminder_date = models.DateField()
	reminder_content = models.TextField(blank=True, null=True)
	done = models.BooleanField(default=False)

	def get_absolute_url(self):
		return "/reminder/" + str(self.id)

	def __str__(self):
		return str(self.id)