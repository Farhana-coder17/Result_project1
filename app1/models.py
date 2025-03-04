from django.db import models

# Create your models here.
class Marks(models.Model):
    rollno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    sub1=models.FloatField()
    sub2=models.FloatField()
