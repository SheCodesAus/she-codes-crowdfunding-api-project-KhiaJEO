
from django.contrib.auth import get_user_model
from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    slug = models.SlugField()

class Project(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField()
    summary = models.CharField(max_length=200)
    goal = models.IntegerField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.CharField(max_length=200)
    # owner = models.ForeignKey(
    #     get_user_model(),
    #     on_delete=models.CASCADE,
    #     related_name='owner_projects'
    # )
    issue = models.CharField(max_length=600)
    tools = models.CharField(max_length=600)
    science = models.CharField(max_length=600) 
    closing_date = models.DateTimeField()
    # categories = models.ManyToManyField(Category, blank = True, null = True) 
    category = models.ForeignKey(
        'Category', 
        null=True, blank=True, 
        on_delete=models.CASCADE, 
        related_name='project_id'
        ) 

# class Category(models.Model):
#     category_name = models.CharField(max_length=200)

    
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

