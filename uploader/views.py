# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
import pdb;

from uploader.models import Document, Report
from uploader.forms import DocumentForm, reportEditForm

def list(request):
	# Handle file upload
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = Document(docfile = request.FILES['docfile'])
			newdoc.save()

			# Redirect to the document list after POST
			return HttpResponseRedirect(reverse('uploader.views.list'))
	else:
		form = DocumentForm() # A empty, unbound form

		# Load documents for the list page
		documents = Document.objects.all()
		reports = Report.objects.all()

		# Render list page with the documents and the form
		return render_to_response(
			'list.html',
			{'reports': reports, 'documents': documents, 'form': form},
			context_instance=RequestContext(request)
		)
		
def editreport(request):
	id = request.POST.get("idofreport", None);
	instance = get_object_or_404(Report, id=id)
	form = reportEditForm(request.POST or None, instance=instance)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('uploader.views.list'))
		
	form = reportEditForm(instance=instance)
	return render_to_response(
		'editreport.html',
		{'form': form, 'idofreport': id},
		context_instance=RequestContext(request)
	)

def deletereport(request):
	id = request.POST.get("idofreport", None);
	Report.objects.get(pk=id).delete()
	
	return HttpResponseRedirect(reverse('uploader.views.list'))	
