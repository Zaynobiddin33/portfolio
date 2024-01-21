from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
import secrets


def token_generate(length=32):
    token = secrets.token_hex(length)
    return token


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
        return redirect('main')
    return render(request, 'new.html')

def mymedia(request):
    
    return render(request, 'sm.html', {'medias': Mymedia.objects.all()})

@login_required(login_url='login')
def dash(request):
    medias = Mymedia.objects.all().count()
    contacts = Message.objects.all().count()
    projects = Projects.objects.all().count()
    users = User.objects.all().count()
    
    context = {
        'medias':medias,
        'contacts':contacts,
        'projects':projects,
        'users': users
    }
    
    return render(request, 'dashboard/index.html', context)

#CRUD contact
def list_contact(request):
    messages = Message.objects.all()
    context = {
        "messages": messages
    }
    return render(request, 'dashboard/contact/list.html', context)

def detail_contact(request, id):
    message = Message.objects.get(id=id)
    context = {
        "message": message
    }
    return render(request, 'dashboard/contact/detail.html', context )

#CRUD Mymedia
def medias(request):
    medias = Mymedia.objects.all()
    context = {
       'medias': medias 
    }
    return render(request, 'dashboard/medias/list.html', context)


def creata_media(request):

    if request.method == "POST":
        name = request.POST['name']
        url = request.POST['url']
        Mymedia.objects.create(
            media_name = name,
            url = url
        )
        return redirect('medias')
        
    return render(request, 'dashboard/medias/create.html')

def  update_media(request, id):
    media = Mymedia.objects.get(id =id)
    if request.method == 'POST':
        media.media_name = request.POST['name']
        media.url = request.POST['url']
        media.save()
        return redirect('medias')
    context = {
        'media': media
    }
    return render(request, 'dashboard/medias/update.html',context)

def delete_media(request, id):
    Mymedia.objects.get(id=id).delete()
    return redirect('medias')

#CRUD projects
def projects(request):
    projects = Projects.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'dashboard/projects/list.html', context)

def creata_project(request):
    if request.method == 'POST':
        name = request.POST['name']
        url = request.POST['url']
        Projects.objects.create(
            name = name,
            url = url
        )
    
    return render(request, 'dashboard/projects/create.html')

def update_project(request, id):
    project = Projects.objects.get(id = id)
    if request.method  == "POST":
        project.name = request.POST['name']
        project.url = request.POST['url']
        project.save()
    context = {
        'project': project
    }
    return render(request, 'dashboard/projects/update.html', context)


def delete_project(request, id):
   Projects.objects.get(id=id).delete()
   return redirect('projects')


#LOGIN
def login_user(request):
    login_error = False
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,  password=password)
        if user:
            login(request, user)
            return redirect('dash')
        else:
            login_error = "Incorrect username or password. Please try again."
    return render(request, 'dashboard/auth/login.html', {"login_error": login_error})


#Faqat admindan taklif olganlar registratsiya qila oladi va bu token olish uchun funksiya
def add_user(request):
    token = token_generate()
    if request.method == "POST":
        Token.objects.create(
            token = token
        )
        return redirect('dash')
    return render(request, 'dashboard/auth/adduser.html', {"token": token})


#registratsiya
def regist(request):
    error = False
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not User.objects.filter(username = username):
            User.objects.create_user(
                username=username,
                password=password
            )
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('dash')
        else:
            error = f"the username {username} already exists"
    return render(request, 'dashboard/auth/register.html', {'error': error})

#Token bilan registratsiyadan o'tish
def regist_token(request):
    error = False
    if request.method == "POST":
        data = request.POST['token']
        if Token.objects.filter(token = data) and Token.objects.get(token = data).is_active == True:
            selected = Token.objects.get(token = data)
            selected.is_active = False
            selected.save()
            return redirect('register')
        else:
            error = 'This token is already used or does not exist'
    return render(request, 'dashboard/auth/tokenauth.html', {'error': error})

#LOGOUT
def logout_user(request):
    logout(request)
    return redirect('login')