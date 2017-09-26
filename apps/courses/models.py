from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors["name"] = "Course name must be more than 5 characters long."
        if len(postData["desc"]) < 15:
            errors["desc"] = "Course description must be more than 15 characters long."

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    objects = CourseManager()