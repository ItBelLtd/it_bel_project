from django.contrib import admin
from .models.author import Author
from .models.user import User


class AuthorAdmin(admin.ModelAdmin):
    pass


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author, AuthorAdmin)
admin.site.register(User, UserAdmin)
