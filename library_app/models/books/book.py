from django.db import models
from library_project.library_app.models.users.author import Author
from django.utils import timezone


class Book(models.Model):
    """Модель книги"""

    book_id = models.AutoField(
        primary_key=True,
        verbose_name="ID книги",
        help_text="Уникальный идентификатор книги",
    )
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name="Название книги",
        help_text="Название книги"
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        verbose_name="ID автора"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание"
    )
    content = models.TextField(
        blank=False,
        null=False,
        verbose_name="Содержание книги",
        help_text="Содержание"
    )
    cover = models.ImageField(
        upload_to='covers/',
        verbose_name="Фото книги",
        help_text="Фотография книги"
    )
    added = models.DateTimeField(
        default=timezone.now,
        verbose_name="Дата добавления",
        help_text="Дата"
    )

    class Meta:
        verbose_name = "Книга"
        verbose_plural = "Книги"