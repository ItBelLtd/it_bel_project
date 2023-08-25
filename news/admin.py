from django.contrib import admin

from .models.comment import Comment
from .models.like import Like
from .models.news import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass
