import imp
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Notes
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import NoteForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'


class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NoteForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.notes.all()
    # template_name="notes/notes_list.html"


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"


class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NoteForm

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})


# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#         return render(request, 'notes/note_detail.html', {'note': note})
#     except Notes.DoesNotExist:
#         raise Http404("Note doesnt exist")
