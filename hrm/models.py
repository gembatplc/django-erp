from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True,null=True)
    def __str__(self):
        return ('name','desription')

class Division(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True,null=True)    