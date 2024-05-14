from django.db import models
from datetime import datetime
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.


class UserDetail(models.Model):
    user_name = models.CharField(max_length=50)
    profile = models.CharField(max_length=50)
    description = CKEditor5Field('Text', config_name='extends')
    photo = models.ImageField(upload_to='media/slider/%Y/')
    github_url = models.CharField(max_length=550)
    linkedin_url = models.CharField(max_length=550)
    user_mail = models.CharField(max_length=550)
    experience = models.IntegerField()
    education = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=datetime.now, blank=True)


class TechStack(models.Model):

    exp_choices = (
        ('basic', 'Basic'),
        ('intermediate', 'Intermediate'),
        ('experienced', 'Experienced'),
    )

    technology = models.CharField(max_length=255)
    experience = models.CharField(choices=exp_choices, max_length=255)


class ToolStack(models.Model):

    exp_choices = (
        ('basic', 'Basic'),
        ('intermediate', 'Intermediate'),
        ('experienced', 'Experienced'),
    )

    tool_soft = models.CharField(max_length=255)
    tool_experience = models.CharField(choices=exp_choices, max_length=255)


class Projects(models.Model):
    proj_name = models.CharField(max_length=50)
    github_link = models.CharField(max_length=50)
    proj_link = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='media/projects/%Y/')
