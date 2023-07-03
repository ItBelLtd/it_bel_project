from django.db import models
from users.models.user import User
from users.models.author import Author
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
    owner_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Какой пользователь оставил',
        null=True,
        blank=True,
    )
    owner_author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Какой автор оставил',
        null=True,
        blank=True,

    )

    def __str__(self) -> str:
        return self.text

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарий"

        constraints = [
            # check for one out of two owner options
            models.CheckConstraint(
                name="one out of two owner options is chosen",
                check=(
                    models.Q(
                        owner_user__isnull=True, owner_author__isnull=False
                    ) | models.Q(
                        owner_user__isnull=False, owner_author__isnull=True
                    )
                ),
            )
        ]
