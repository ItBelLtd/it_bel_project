from django.db import models
from users.models.user import User
from django.utils import timezone
from .news import News


class Comment(models.Model):
    comment_id = models.AutoField(
        primary_key=True,
        verbose_name='ID комментария',
    )
    text = models.TextField(
        max_length=300,
        verbose_name='Текст комментария',
    )
    added = models.DateTimeField(
        default=timezone.now,
        verbose_name='Дата добавления',
    )
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Какой пользователь оставил',
        null=True,
        blank=True,
    )
    as_author = models.BooleanField(
        verbose_name='Комментарий от автора',
        default=False,
    )

    def __str__(self) -> str:
        return self.text

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарий"