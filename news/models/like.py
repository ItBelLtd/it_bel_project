from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone


class Like(models.Model):
    LIKE = 1
    DISLIKE = -1

    VOTES = (
        (DISLIKE, 'Не нравится'),
        (LIKE, 'Нравится')
    )

    vote = models.SmallIntegerField(
        verbose_name='Голос',
        choices=VOTES,
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='likes',
        verbose_name='Пользователь',
    )
    content_type = models.ForeignKey(

        ContentType,
        on_delete=models.CASCADE,
        verbose_name='Тип контента',
    )
    added = models.DateTimeField(
        verbose_name='Время добавления',
        default=timezone.now,
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f'{self.user} liked {self.content_type}: {self.content_object}'

    class Meta:
        ordering = ['-added']

        verbose_name = "Лайк"
        verbose_name_plural = "Лайки"
