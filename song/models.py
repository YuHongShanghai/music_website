from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Singer(models.Model):
    name=models.CharField(max_length=250)

    class Meta:
        ordering=('name',)

    def __str__(self):
        return self.name


class Song(models.Model):
    name=models.CharField(max_length=250)
    singer=models.ForeignKey(Singer,on_delete=models.CASCADE,related_name='songs')
    slug=models.SlugField(max_length=250,db_index=True, unique=True)
    file=models.FileField(upload_to='song_files/audio',blank=True)
    poster=models.ImageField(upload_to='song_files/poster',blank=True)
    users=models.ManyToManyField(User,blank=True)

    def get_absolute_url(self):
        return reverse('song:song_detail',args=[self.slug])

    class Meta:
        ordering=('slug',)

    def __str__(self):
        return self.name+" - "+self.singer.name
