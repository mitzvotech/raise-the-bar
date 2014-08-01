from django.shortcuts import render
from app.models import *
from app.forms import *
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, QueryDict, HttpResponseRedirect
from datetime import datetime
from django.views.generic import ListView

# Create your views here.

@login_required
def home(request):
	return HttpResponseRedirect("/firm")

@login_required
def firm_view(request, firm_id):
	firm = Firm.objects.get(pk=firm_id)
	notes = Note.objects.filter(firm__id=firm_id)
	reminders = Reminder.objects.select_related("note")
	return render(request, 'firm_view.html', {'firm':firm, 'notes':notes, 'reminders':reminders}, context_instance=RequestContext(request))

@login_required
def contact_view(request, contact_id):
	contact = Contact.objects.get(pk=contact_id)
	notes = Note.objects.filter(contact__id=contact_id)
	reminders = Reminder.objects.select_related("note")
	return render(request, 'contact_view.html', {'contact':contact, 'notes':notes, "reminders":reminders}, context_instance=RequestContext(request))

@login_required
def note_view(request, note_id):
	note = Note.objects.get(pk=note_id)
	reminders = Reminder.objects.filter(note__id=note_id)
	return render(request, 'note_view.html', {'note':note, 'reminders':reminders}, context_instance=RequestContext(request))

@login_required
def reminder_view(request, reminder_id):
	reminder = Reminder.objects.get(pk=reminder_id)
	return render(request, 'reminder_view.html', {'reminder':reminder}, context_instance=RequestContext(request))


@login_required
def add_contact(request):
	if request.method == "POST":
			if request.is_ajax():
				d = QueryDict(request.body)
				c, created = Contact.objects.get_or_create(first_name=d["first_name"],last_name=d['last_name'],title=d['title'],email=d['email'],phone_number=d['phone_number'],contact_notes=d['contact_notes'],firm=Firm.objects.get(pk=int(d['firm'])))
				return HttpResponse('"' + str(c.id) + "," + str(created) + '"')
	return HttpResponseRedirect("/firm/" + str(firm_id))

@login_required
def add_note(request, firm_id):
	if request.method == "POST":
		n = Note()
		print request.POST
		n.firm = Firm.objects.get(pk=firm_id)
		n.user = request.user
		n.contact = Contact.objects.get(pk=request.POST["contact-select"])
		n.content = request.POST["content"]
		n.save()
		if request.POST['reminder_date'] != "":
			r = Reminder()
			r.note = n
			r.reminder_date = datetime.strptime(request.POST['reminder_date'],"%m/%d/%Y")
			r.reminder_content = request.POST['reminder_content']
			r.save()
		return HttpResponseRedirect(reverse('firm-view', args=(firm_id,)))	

	else:
		firm = Firm.objects.get(pk=firm_id)
		n = NoteForm()
		rform = ReminderForm()
		cform = ContactForm()
		contacts = Contact.objects.filter(firm__id =firm_id).order_by("last_name","first_name")
	return render(request, 'add_note.html', {'firm':firm, 'nform': n, 'cform': cform, 'rform':rform, 'contacts': contacts}, context_instance=RequestContext(request))