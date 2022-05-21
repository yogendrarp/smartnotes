import imp
from django.http import Http404
from django.shortcuts import render
from .models import Notes
from django.views.generic import ListView, DetailView, CreateView
from .forms import NoteForm
# Create your views here.


class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NoteForm


class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    # template_name="notes/notes_list.html"


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})


# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#         return render(request, 'notes/note_detail.html', {'note': note})
#     except Notes.DoesNotExist:
#         raise Http404("Note doesnt exist")
