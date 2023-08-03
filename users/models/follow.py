from django.db import models

from users.models.author import Author
from users.models.user import User


class Follow(models.Model):
    """Модель подписки на пользователей"""
    follow_id = models.AutoField(
        primary_key=True,
        verbose_name="ID пользователя"
    )
    follower = models.ForeignKey(
        User,
        related_name='follows',
        verbose_name='Подписчик',
        on_delete=models.CASCADE,

    )
    author = models.ForeignKey(
        Author,
        related_name='following',
        verbose_name='Автор',
        on_delete=models.CASCADE,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['follower', 'author', ],
                name='Unique follow'
            )
        ]
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
