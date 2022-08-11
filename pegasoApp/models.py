from django.db import models
from django.utils import timezone
 
class taskDB(models.Model):
    task = models.CharField(max_length=30)
    priority = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    time_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.task