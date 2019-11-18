from django.shortcuts import render,get_object_or_404
from .models import Song,Tag
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


def song_list(request):
    sort=request.GET.get('sort','0')
    word=request.GET.get('search_word','')
    songs=Song.objects.filter(Q(name__icontains = word) | Q(singer__name__icontains = word))
    if sort=='1':
        songs = songs.order_by("singer__name")
    paginator=Paginator(songs,10)
    page=request.GET.get('page')
    try:
        songs=paginator.page(page)
    except PageNotAnInteger:
        songs = paginator.page(1)
    except EmptyPage:
        songs = paginator.page(paginator.num_pages)

    return render(request, 'list.html', {'songs': songs,'search_word': word,'sort':sort})


def song_detail(request,song_slug):
    if request.method=='POST':
        tag_name=request.POST['tag_name']
        data = {}
        if len(tag_name)>8:
            data['msg']='long'
            return JsonResponse(data)
        if len(tag_name)==0:
            data['msg']='short'
            return JsonResponse(data)
        song = get_object_or_404(Song, slug=song_slug)

        try:
            t=song.tags.get(name=tag_name)
            t.num += 1
            t.save()
        except Tag.DoesNotExist:
            tag = Tag()
            tag.name = tag_name
            tag.save()
            song.tags.add(tag)
        data['msg']='success'
        return JsonResponse(data)
    else:
        song=get_object_or_404(Song,slug=song_slug)
        return render(request,'detail.html',{'song':song})

def get_tag_data(request,song_slug):
    song = get_object_or_404(Song, slug=song_slug)
    data={}
    for tag in song.tags.all():
        data[tag.name]=str(tag.num)
    return JsonResponse(data)



