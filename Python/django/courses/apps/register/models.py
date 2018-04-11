from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = 'Course name must be at least 5 charaters'
        if len(postData['desc']) < 15:
            errors['desc'] = 'Description must be at least 15 charaters'
        return errors



class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    objects = CourseManager()