from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='account'

urlpatterns=[
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('register/',views.user_register,name='register'),
    path('mysongs/',views.my_songs,name='mysongs'),
    path('removesong/',views.remove_song,name='removesong'),
]

