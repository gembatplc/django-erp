from django.db import models

# Create your models here.
class Department(models.Model):
  title = models.charField(max_length=100)
