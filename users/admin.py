from django.contrib import admin

from .models.author import Author
from .models.user import User


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
