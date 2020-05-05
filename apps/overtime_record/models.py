from django.db import models

class Overtime_record(models.Model):
    reason = models.CharField(max_length=100, help_text='Overtime reason')

    def __str__(self):
        return self.reason