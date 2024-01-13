from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.

def main(request):
    projects = Projects.objects.all()
    forms = Message.objects.all()
    medias = Mymedia.objects.all()
    context = {
        "forms" : forms,
        "medias" : medias,
        "projects" : projects
    }
    return render(request, 'data.html', context)

def form(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        text = request.POST['text']
        Message.objects.create(
            name = name,
            email = email,
            text = text
        )
    return render(request, 'new.html')

def mymedia(request):
    return render(request, 'sm.html')