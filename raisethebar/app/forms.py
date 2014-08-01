from django import forms
from django.forms import ModelForm, Textarea
from app.models import *

class NoteForm(ModelForm):
	class Meta:
		model = Note
		exclude = ['firm, contact','user']
		widgets = {
            'content': Textarea(attrs={'class': 'form-control'}),
        }

class ContactForm(ModelForm):
	class Meta:
		model = Contact
		exclude = ['firm']

class ReminderForm(ModelForm):
	class Meta:
		model = Reminder
		exclude = ['note']
		widgets = {
            'reminder': forms.DateInput(attrs={'class': 'form-control'}),
        }