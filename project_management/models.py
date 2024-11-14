from django.db import models

class Project(models.Model):
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  start_date = models.DateField(null=True)
  end_date = models.DateField(null=True)
 