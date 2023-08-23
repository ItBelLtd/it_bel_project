from django.db import models


class Tag(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name='Название тега',
    )
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Тег'

    def __str__(self) -> str:
        return self.name
