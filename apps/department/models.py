from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=60, help_text='Department name')

    def __str__(self):
        return self.name

