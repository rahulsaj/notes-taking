from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import EntryForm
from .models import Entry


# Create your views here.
def index(request):
    notes = Entry.objects.all().order_by("-updated_on")
    return render(request, "notes/index.html", {"notes": notes})


def add_note(request):
    form = EntryForm()
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            entry = Entry(title=data["title"], body=data["body"])
            entry.save()
            return redirect(entry.get_absolute_url())
    return render(request, "notes/new_note.html", {"form": form})


def get_note(request, id):
    data = Entry.objects.get(pk=id)
    return render(request, "notes/note.html", {"data": data})


def delete_note(request, id):
    data = Entry.objects.get(pk=id)
    data.delete()
    return redirect("home")


def edit_note(request, id):
    data = get_object_or_404(Entry, pk=id)
    form = EntryForm(instance=data)
    if request.method == "POST":
        form = EntryForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect(data.get_absolute_url())
    return render(request, "notes/edit_note.html", {"form": form})
