from django import forms
from .models import Tickets, Employee, Departments, Comments

class FormTicket(forms.ModelForm):
	subject = forms.CharField(required=True, max_length=350)
	description = forms.CharField(widget=forms.Textarea(), required=True)
	STATUS_CHOICES = (
			('open','OPEN'),
			('closed', 'CLOSED'),
			('fixed', 'FIXED'),
			('in_progress', 'IN PROGRESS'),
			('reopened','REOPENED')
		)
	status = forms.ChoiceField(choices=STATUS_CHOICES)

	PRIORITY_CHOICES = (
			('low', 'LOW'),
			('medium', 'MEDIUM'),
			('high', 'HIGH'),
			('critical', 'CRITICAL')
		)
	priority = forms.ChoiceField(choices=PRIORITY_CHOICES)

	department_id = forms.ModelChoiceField(queryset=Departments.objects.values_list('department_id', flat=True))
	ticket_owner = forms.ModelChoiceField(queryset=Employee.objects.all())
	assign_to = forms.ModelChoiceField(queryset=Employee.objects.all())

	class Meta:
		model = Tickets
		fields = ('subject', 'description', 'status', 'priority','department_id', 'ticket_owner', 'assign_to' )


class DepartmentForm(forms.Form):
    department = forms.ChoiceField(choices = [])

    def __init__(self, *args, **kwargs):
        super(MatchForm, self).__init__(*args, **kwargs)
        self.fields['department'].choices = [(x.pk, x.get_full_name()) for x in Departments.objects.all()]
	