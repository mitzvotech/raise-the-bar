from django.shortcuts import render
from app.models import *
from app.forms import *
from django.template import RequestContext


# Create your views here.

def notes(request):
	if request.method == "POST":
		pass
	else:
		n = NoteForm()
	return render(request, 'add_note.html', {'form': n}, context_instance=RequestContext(request))