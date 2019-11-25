from django.urls import path
from . import views

app_name='song'

urlpatterns=[
    path('',views.song_list,name='song_list'),
    path('<slug:song_slug>/',views.song_detail,name='song_detail'),
]
