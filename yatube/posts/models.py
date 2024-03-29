from django.db import models
from django.contrib.auth import get_user_model


LIMIT = 100

User = get_user_model()


class Post(models.Model):
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )
    group = models.ForeignKey(
        'Group',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Группы',
        related_name='posts'
    )

    def __str__(self):
        return self.text[:LIMIT]

    class Meta:
        ordering = ('-pub_date',)


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Загаловок')
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name='Описание группы')

    def __str__(self):
        return self.title
