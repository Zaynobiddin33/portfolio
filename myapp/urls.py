from django.urls import path
from .views import *
urlpatterns =[
    path('', main),
    path('form', form),
    path('urls', mymedia),
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

]
