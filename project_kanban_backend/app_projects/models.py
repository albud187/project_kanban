from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse
from django.template.defaultfilters import slugify
from datetime import datetime
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    #use many to many relationship
    owners = models.ManyToManyField(User)
    members = models.ManyToManyField(User)

class Task(models.model):
    creator = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=120)
    description = models.TextField()
    parent_project = models.foreignKey(Project, on_delete=models.CASCADE)
    TASK_STATUSES = [
    ('REC', 'recieved'),
    ('PLA', 'planning'),
    ('WIP', 'work in progress'),
    ('UNR', 'under review'),
    ('COM', 'completed')
    ]
    task_status = models.CharField(max_length=3, choices = TASK_STATUSES, blank= True, null = True)

    critical = models.BooleanField(default=False)
    urgent = models.BooleanField(default=False)
