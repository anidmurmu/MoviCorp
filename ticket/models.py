from django.db import models
from django.contrib import admin


# Create your models here.

# 'departments' table
class Departments(models.Model):
	class Meta:
		verbose_name_plural = "departments"

	department_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=250)
	
	def __str__(self):
		return self.name

class DepartmentsAdmin(admin.ModelAdmin):
	list_display=('department_id', 'name')

# 'employee' table
class Employee(models.Model):
	class Meta:
		verbose_name_plural = "employee"

	emp_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=250)
	email_id = models.EmailField(max_length=250)
	password = models.CharField(max_length=250)
	department_id = models.ForeignKey(Departments, null=True, on_delete=models.SET_NULL)
	is_admin = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)

class EmployeeAdmin(admin.ModelAdmin):
	list_display = ('emp_id', 'name', 'email_id', 'password', 'department_id', 'is_admin', 'is_active')


# 'tickets' table
class Tickets(models.Model):
	class Meta:
		verbose_name_plural = "tickets"

	ticket_id = models.AutoField(primary_key=True)
	subject = models.CharField(max_length=350)
	description = models.TextField()

	STATUS_CHOICES = (
			('open','OPEN'),
			('closed', 'CLOSED'),
			('fixed', 'FIXED'),
			('in_progress', 'IN PROGRESS'),
			('reopened','REOPENED')
		)
	status  = models.CharField(max_length=30, choices=STATUS_CHOICES)

	PRIORITY_CHOICES = (
			('low', 'LOW'),
			('medium', 'MEDIUM'),
			('high', 'HIGH'),
			('critical', 'CRITICAL')
		)
	priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)

	department_id = models.ForeignKey(Departments, null=True, on_delete=models.SET_NULL)
	created_date = models.DateTimeField(auto_now_add=True)
	ticket_owner = models.CharField(max_length=250)
	assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE)

class TicketsAdmin(admin.ModelAdmin):
	list_display = ('ticket_id', 'subject', 'description', 'status', 'priority', 'department_id', 'created_date', 'ticket_owner', 'assigned_to')


# 'comments' table
class Comments(models.Model):
	class Meta:
		verbose_name_plural = "comments"
	
	comment_id = models.AutoField(primary_key=True)
	message = models.TextField()
	ticket_id = models.ForeignKey(Tickets, on_delete=models.CASCADE)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)
	emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)


class CommentsAdmin(admin.ModelAdmin):
	list_display = ('comment_id', 'message', 'ticket_id', 'created_date', 'modified_date', 'emp_id')

