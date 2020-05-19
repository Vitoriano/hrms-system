from .models import Employee
from django.views.generic import ListView

class EmployeeList(ListView):
    model = Employee