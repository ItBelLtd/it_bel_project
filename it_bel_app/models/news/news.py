from django.db import models
from it_bel_app.models.users.author import Author
from django.utils import timezone


class News(models.Model):
    """Модель новости"""

    news_id = models.AutoField(
        primary_key=True,
        verbose_name="ID книги",
        help_text="Уникальный идентификатор новости",
    )
    title = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        verbose_name="Заголовок новости",
        help_text="Заголовок новости"
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        verbose_name="ID автора"
    )
    description = models.TextField(
        blank=True,
        null=True,
        max_length=25,
        verbose_name="Описание новости"
    )
    content = models.TextField(
        blank=False,
        null=False,
        verbose_name="Содержание",
        help_text="Содержание"
    )
    cover = models.ImageField(
        upload_to='covers/',
        verbose_name="Фото",
        help_text="Фотографии"
    )
    added = models.DateTimeField(
        default=timezone.now,
        verbose_name="Дата добавления",
        help_text="Дата"
    )

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"