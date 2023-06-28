from django.db import models
from django.utils import timezone


class Author(models.Model):


    author_id = models.AutoField(
        primary_key=True,
        verbose_name="ID автора"
    )
    name = models.CharField(
        verbose_name="Имя автора",
        max_length=150,
        unique=True,
        null=True,
        blank=True
    )
    email = models.EmailField(
        blank=False,
        null=False,
        verbose_name="Почта автора",
        help_text="Email"
    )
    date_joined = models.DateTimeField(
        verbose_name="Дата регистрации",
        default=timezone.now
    )
    is_active = models.BooleanField(
        verbose_name="Активный",
        default=True
    )

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"