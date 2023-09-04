from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

from ..managers.user import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """Модель пользователя"""

    user_id = models.AutoField(
        primary_key=True,
        verbose_name="ID пользователя"
    )
    username = models.CharField(
        verbose_name="Имя пользователя",
        max_length=150,
        unique=True,
        null=True,
        blank=True
    )
    email = models.EmailField(
        blank=False,
        null=False,
        verbose_name="Почта пользователя",
        help_text="Email",
        unique=True,
    )
    date_joined = models.DateTimeField(
        verbose_name="Дата регистрации",
        default=timezone.now,
    )
    is_staff = models.BooleanField(
        verbose_name="Админ",
        default=False
    )
    is_superuser = models.BooleanField(
        verbose_name='Супер',
        default=False
    )
    is_active = models.BooleanField(
        verbose_name="Активный",
        default=True
    )
    is_moderator = models.BooleanField(
        verbose_name="Модератор",
        default=False
    )

    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return f"{self.username} ({self.email})"

    def get_date(self):
        day = self.date_joined.day
        month = self.date_joined.month
        year = self.date_joined.year
        return f"{day} {month} {year}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['-date_joined']
