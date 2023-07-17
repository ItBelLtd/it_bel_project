from django.contrib import admin

from .models.comment import Comment
from .models.news import News


class NewsAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentAdmin)
