from django.contrib import admin
from .models import Singer,Song

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}

admin.site.register(Singer)

