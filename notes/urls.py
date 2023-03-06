from django.urls import  path
from . import  views

urlpatterns =[
    path('notes', views.list, name = 'notes.list'),
    path('notes/<int:pk>', views.detail, name = 'notes.detail'),
    path('notes/new', views.NotesCreateView.as_view(), name='notes.new'),
]