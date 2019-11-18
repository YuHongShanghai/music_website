from django.urls import path
from . import views

app_name='song'

urlpatterns=[
    path('',views.song_list,name='song_list'),
    path('<slug:song_slug>/',views.song_detail,name='song_detail'),
    path('<slug:song_slug>/get_tag_data/', views.get_tag_data, name="get_tag_data"),
]
