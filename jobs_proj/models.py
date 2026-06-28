from django.db import models


class Vacancy(models.Model):

    title = models.CharField(
        max_length=200
    )

    company = models.CharField(
        max_length=200
    )

    location = models.CharField(
        max_length=100
    )

    experience = models.CharField(
        max_length=100
    )

    salary = models.CharField(
        max_length=100
    )

    description = models.TextField()

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class Article(models.Model):

    title = models.CharField(
        max_length=200,
        verbose_name="Заголовок"
    )

    short_description = models.TextField(
        verbose_name="Короткий опис"
    )

    content = models.TextField(
        verbose_name="Текст статті"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title