from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def all_tickets( request ):
	return render( request, "ticket/list.html", {})
	#return HttpResponse('<h1> This is Sparta! </h1>')