from django import forms
from django.forms import ModelForm
from app.models import *

class NoteForm(ModelForm):
	class Meta:
		model = Note
		exclude = ['firm']