from django.shortcuts import render
from app.models import *
from app.forms import *
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, QueryDict, HttpResponseRedirect
import datetime

# Create your views here.

def home(request):
	return HttpResponse("hello")

def firm_view(request, firm_id):
	firm = Firm.objects.get(pk=firm_id)
	notes = Note.objects.filter(firm__id=firm_id)
	return render(request, 'firm_view.html', {'firm':firm, 'notes':notes}, context_instance=RequestContext(request))

def add_contact(request):
	if request.method == "POST":
			if request.is_ajax():
				d = QueryDict(request.body)
				c, created = Contact.objects.get_or_create(first_name=d["first_name"],last_name=d['last_name'],email=d['email'],phone_number=d['phone_number'],firm=Firm.objects.get(pk=int(d['firm'])))
				return HttpResponse('"' + str(c.id) + "," + str(created) + '"')
	return HttpResponseRedirect("/firm/" + str(firm_id))

#@login_required
def add_note(request, firm_id):
	if request.method == "POST":
		n = Note()
		print request.POST
		n.firm = Firm.objects.get(pk=firm_id)
		n.user = request.user
		n.contact = Contact.objects.get(pk=request.POST["contact-select"])
		n.content = request.POST["content"]
		n.save()
#		return HttpResponseRedirect(reverse('/firm-view/', + str(firm_id))
		return HttpResponseRedirect(reverse('firm-view', args=(firm_id,)))	

	else:
		firm = Firm.objects.get(pk=firm_id)
		n = NoteForm()
		cform = ContactForm()
		contacts = Contact.objects.filter(firm__id =firm_id).order_by("last_name","first_name")
	return render(request, 'add_note.html', {'firm':firm, 'nform': n, 'cform': cform, 'contacts': contacts}, context_instance=RequestContext(request))