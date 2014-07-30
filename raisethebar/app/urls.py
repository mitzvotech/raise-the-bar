from django.conf.urls import patterns, include, url
from django.views.generic import ListView, CreateView
from app.models import Firm

urlpatterns = patterns('',
    # Examples:
#    url(r'^notes/$', 'app.views.notes', name='notes'),
 	url(r'^addcontact$', 'app.views.add_contact', name='contact-add'),
	url(r'^firm/$', ListView.as_view(queryset=Firm.objects.order_by("firm_name"))),
	url(r'^firm/add/$', CreateView.as_view(model=Firm,)),
 	url(r'^firm/(?P<firm_id>[0-9]+)/$', 'app.views.firm_view', name='firm-view'),
	url(r'^firm/addnote/(?P<firm_id>[0-9]+)/$', 'app.views.add_note', name='note-add'),
	url(r'^$', 'app.views.home')
)