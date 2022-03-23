from django.contrib.auth import get_user_model
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField() 

class Project(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    image = models.URLField()
    goal = models.IntegerField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    # owner = models.CharField(max_length=200)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )
    # categories = models.ManyToManyField(Category, blank = True, null = True)
    
class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    supporter =  models.CharField(max_length=200)
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.CharField(max_length=200)

