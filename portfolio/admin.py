from django.contrib import admin

#import the Project model from portfolio/models.py
from portfolio.models import Project

# Register your models here.

admin.site.register(Project)