from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(primary_key=True)
    address = models.TextField()
    father_name = models.TextField(default="janina")
    
    