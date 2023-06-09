from django.contrib import admin
from .models import Video, Comment, ViewCount

admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(ViewCount)
# Register your models here.
