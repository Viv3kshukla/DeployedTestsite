from django.db import models

# Create your models here.

class Data(models.Model):
    primary_field=models.IntegerField(primary_key=True)
    first_field=models.CharField(max_length=20,blank=True,null=True)
    second_field=models.CharField(max_length=20,blank=True,null=True)
    third_field = models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return str(self.primary_field)