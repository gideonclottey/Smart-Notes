from django.shortcuts import render
from .models import Notes
from django.http import Http404
from django.views.generic import  CreateView, UpdateView
from .forms import NotesForm

# Create your views here.

def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html',{'notes':all_notes})

def detail(request,pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Notes doesn't exist")
    return render(request,'notes/notes_detail.html',{'note':note})

#using classed based views

class NotesCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'

class NotesUpdateView(UpdateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'