from django.urls import path
from .views import *

urlpatterns =[
    path('', main, name='main'),
    path('form/', form, name='form'),
    path('urls/', mymedia),
    #dashboard
    path('dashboard', dash , name = 'dash'),
    #contact
    path('contacts', list_contact, name = 'list_contact'),
    path('contacts/detail/<int:id>/', detail_contact, name = 'detail_contact'),
    #Mymedia
    path('medias', medias, name='medias'),
    path('medias/create', creata_media, name = 'create_media'),
    path('medias/update/<int:id>/', update_media, name = 'update_media'),
    path('medias/delete/<int:id>/', delete_media, name = 'delete_media'),
    #Projects
    path('projects', projects, name='projects'),
    path('projects/create', creata_project, name = 'create_project'),
    path('projects/update/<int:id>/', update_project, name = 'update_project'),
    path('projects/delete/<int:id>/', delete_project, name = 'delete_project'),
    #user management
    path('login/', login_user, name='login'),
    path('adduser', add_user, name='add_admin'),
    path('first-step', regist_token, name = 'regist_token'),
    path(f"register/", regist, name = 'register'),
    path('logout', logout_user, name = "logout_user")
]
