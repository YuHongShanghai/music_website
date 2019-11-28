from django.shortcuts import render,get_object_or_404
from .models import Song
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.http import HttpResponseRedirect
from django.urls import reverse

def song_list(request):
    sort=request.GET.get('sort','0')
    word=request.GET.get('search_word','')
    songs=Song.objects.filter(Q(name__icontains = word) | Q(singer__name__icontains = word))
    if sort=='1':
        songs = songs.order_by("singer__name")
    paginator=Paginator(songs,10)
    page=request.GET.get('page')
    all_songs=songs
    try:
        songs=paginator.page(page)
    except PageNotAnInteger:
        songs = paginator.page(1)
    except EmptyPage:
        songs = paginator.page(paginator.num_pages)
    return render(request, 'list.html', {'all_songs':all_songs,'songs': songs,'search_word': word,'sort':sort,'user':request.user})


def song_detail(request,song_slug):
    song=get_object_or_404(Song,slug=song_slug)
    return render(request,'detail.html',{'song':song,'user':request.user})


def index(request):
    return HttpResponseRedirect(reverse('song:song_list'))

