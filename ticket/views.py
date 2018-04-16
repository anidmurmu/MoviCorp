from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from ticket.models import Tickets, Employee, Departments, Comments
from ticket.forms import FormTicket
# Create your views here.

def all_tickets( request ):
	return render( request, "ticket/list.html", {})
	#return HttpResponse('<h1> This is Sparta! </h1>')


def login_view( request ):
	if request.method == 'POST':
		#return render( request, 'hi', {})
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			#login the user
			user = form.get_user()
			login(request, user)
			return redirect('ticket:all_tickets')
	else:
		form = AuthenticationForm()
	return render( request, 'ticket/login.html', {'form': form})	

def list_view(request):
	data = Tickets.objects.all()
	return render(request, 'ticket/list.html', {'data':data})


def info_view(request):
	data = Tickets.objects.get(ticket_id=1)
	data_
	return render(request, 'ticket/info.html', {'data':data})

# def add_ticket_view(request):
# 	print ('apple')
# 	form = FormTicket()
# 	departments = Departments.objects.all()
# 	employee = Employee.objects.all()
# 	return render(request, 'ticket/ticket_form.html', {'form': form, 'employee': employee, 'departments': departments})

def add_ticket_view(request):
	if request.method == 'POST':
		form = FormTicket(request.POST)
		if form.is_valid():
			form_items = form.save(commit=False)
			form_itmes.department_id = Departments.objects.all()
			form_items.save()
		return redirect('ticket:add_ticket')
	else:
		form = FormTicket()
	return render(request, 'ticket/ticket_form.html', {'form': form})