from django.contrib import admin
from .models import Inbox, Setting, Dislike, Like, UserPhoto, Match, Profile

admin.site.register(Profile)
admin.site.register(Inbox)
admin.site.register(Dislike)
admin.site.register(Setting)
admin.site.register(UserPhoto)
admin.site.register(Match)
admin.site.register(Like)

# Register your models here.
