from django import forms
from django.forms import ModelForm

class FormTicket(forms.ModelForm):
	subject = forms.CharField(required=True, max_length=350)
	#description = forms.TextField()
	#status = forms.ModelChoiceField(queryset=models.Tickets.objects.all().status)
	#priority = forms.ModelChoiceField(queryset=models.Tickets.objects.none())
	# department = 
	# created_date = 
	# ticket_owner = 
	# assigned_to = 