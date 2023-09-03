from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils import timezone

from .like import Like
from .tag import Tag
from users.models.author import Author


class News(models.Model):
    """Модель новости"""

    news_id = models.AutoField(
        primary_key=True,
        verbose_name="ID книги",
        help_text="Уникальный идентификатор новости",
    )
    title = models.CharField(
        max_length=70,
        blank=False,
        null=False,
        verbose_name="Заголовок новости",
        help_text="Заголовок новости"
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        verbose_name="ID автора",
        related_name='news'
    )
    description = models.TextField(
        blank=True,
        null=True,
        max_length=60,
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
    is_moderated = models.BooleanField(
        verbose_name='Просмотрена ли модераторами',
        default=False,
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Теги',
        blank=True
    )
    votes = GenericRelation(Like)

    @property
    def total_likes(self) -> int:
        return self.votes.filter(vote=Like.LIKE).count()

    @property
    def total_dislikes(self) -> int:
        return self.votes.filter(vote=Like.DISLIKE).count()

    @property
    def sum_rating(self) -> int:
        return self.votes.aggregate(models.Sum('vote')).get('vote__sum') or 0

    def __str__(self):
        return self.title

    def get_date(self):
        day = self.added.day
        month = self.added.month
        year = self.added.year
        return f"{day} {month} {year}"

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-added']
