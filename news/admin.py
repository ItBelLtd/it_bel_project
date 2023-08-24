from django.contrib import admin

from .models.comment import Comment
from .models.like import LikeDislike
from .models.news import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(LikeDislike)
class LikeAdmin(admin.ModelAdmin):
    pass
