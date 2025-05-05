from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    heading=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    completed=models.BooleanField(default=False)
    due=models.DateTimeField(null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)
    category=models.ForeignKey('Category',on_delete=models.SET_NULL,null=True,blank=True,default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.heading


class Category(models.Model):
    name=models.CharField(max_length=100)    
    def __str__(self):
        return self.name
    