from django.shortcuts import render

from projects.models import Project


# Create your views here.
def all_projects(request):
    # query the database to return all project objects
    projects = Project.objects.all()
    return render(request, 'projects/all_projects.html',
                  {'projects': projects})


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'projects/detail.html', {'project': project})

def home(request):
    return render(request, 'projects/home.html')

def contacts(request):
    return render(request, 'projects/contacts.html')
