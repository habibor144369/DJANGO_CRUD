from django.shortcuts import redirect, render
from First_App .models import Musician, Album
from First_App import forms
from django.db.models import Avg
# Create your views here.

def Index(request):
    musician_list = Musician.objects.order_by('first_name')
    context = {
        "title": "Home Page",
        "musician_list": musician_list,
    }
    return render(request, 'index.html', context)


# Album_list Here....
def Album_List(request, artist_id, username):
    artist_info = Musician.objects.get(pk=artist_id)
    album_list = Album.objects.filter(artist=artist_id).order_by("name")
    artist_reting = Album.objects.filter(artist=artist_id).aggregate(Avg('num_stars'))
    context = {
        "title": "Album List",
        "artist_info": artist_info,
        "album_list": album_list,
        "artist_reting": artist_reting,
    }
    return render(request, 'album_list.html', context)


# Musician Form Here....
def Musician_Form(request):
    form = forms.MusicianForm()

    if request.method == "POST":
        form = forms.MusicianForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('First_App:index')

    context = {
        "title": "Musician Form",
        "form": form
    }
    return render(request, 'musician_form.html', context)


# Album Form Here...
def Album_Form(request):
    form = forms.AlbumForm()

    if request.method == "POST":
        form = forms.AlbumForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('First_App:index')

    context = {
        "title": "Album Form",
        "form": form
    }
    return render(request, 'album_form.html', context)


def Edit_Artist(request, artist_id, username):
    artist_info = Musician.objects.get(pk=artist_id)
    form = forms.MusicianForm(instance=artist_info)

    if request.method == 'POST':
        form = forms.MusicianForm(request.POST, instance=artist_info)
        if form.is_valid():
            form.save(commit=True)
            return Album_List(request, artist_id, username)

    context = {
        "form": form,
    }
    return render(request, 'edit_artist.html', context)


def Edit_Album(request, album_id, username):
    album_info = Album.objects.get(pk=album_id)
    form = forms.AlbumForm(instance=album_info)

    if request.method == 'POST':
        form = forms.AlbumForm(request.POST, instance=album_info)
        if form.is_valid():
            form.save(commit=True)
            return redirect('First_App:index')

    context = {
      "form": form,
      "album_id": album_id
    }
    return render(request, 'edit_album.html', context)


def Delete_Album(request, album_id):
    album = Album.objects.get(pk=album_id).delete()
    return redirect('First_App:index')
    context = {}
    return render(request, "deleted_album.html", context)


def Delete_Musician(request, artist_id):
    musucian = Musician.objects.get(pk=artist_id).delete()
    return redirect('First_App:index')
    context = {}
    return render(request, "delete_musician.html", context)
