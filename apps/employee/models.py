from django.contrib.auth.models import User
from django.db import models
from apps.department.models import Department
from apps.company.models import Company

class Employee(models.Model):
        name = models.CharField(max_length=100, help_text='Employee name')
        user = models.OneToOneField(User, on_delete=models.PROTECT)
        departments = models.ManyToManyField(Department)
        company = models.ForeignKey(Company, on_delete=models.PROTECT)

        def __str__(self):
            return self.name

