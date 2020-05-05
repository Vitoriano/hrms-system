from django.db import models
from apps.employee.models import Employee

class Overtime_record(models.Model):
    reason = models.CharField(max_length=100, help_text='Overtime reason')
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)

    def __str__(self):
        return self.reason