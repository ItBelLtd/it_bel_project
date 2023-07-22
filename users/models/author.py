from django.db import models
from django.utils import timezone

from .user import User


class Author(models.Model):
    """Модель автора"""

    author_id = models.AutoField(
        primary_key=True,
        verbose_name="ID автора"
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='author',
        null=True,
        blank=True,
    )
    name = models.CharField(
        verbose_name="Имя автора",
        max_length=150,
        null=False,
        blank=False
    )
    surname = models.CharField(
        verbose_name="Фамилия автора",
        max_length=150,
        null=False,
        blank=False
    )
    age = models.IntegerField(
        verbose_name="Возраст автора",
        null=False,
        blank=False,
        help_text="Возраст"
    )
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
        verbose_name="Почта автора",
        help_text="Email"
    )
    date_joined = models.DateTimeField(
        verbose_name="Дата регистрации",
        default=timezone.now,
    )
    is_active = models.BooleanField(
        verbose_name="Активный",
        default=False
    )

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
