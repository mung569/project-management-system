from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Project

def project_management(request):
    template = loader.get_template('project_management\master.html')
    return HttpResponse(template.render())

def home(request):
    return render(request, 'home.html')

'''
# Test loading of projects page

def project_management(request):
    projects = Project.objects.all().values()
    template = loader.get_template('project_management\project.html')
    context = {
        'projects': projects,
    }
    return HttpResponse(template.render(context, request))

'''