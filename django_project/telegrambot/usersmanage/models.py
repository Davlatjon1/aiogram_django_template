from django.db import models
from data.config import LANGUAGE_RU, LANGUAGE_UZ, LANGUAGE_EN
from uuid import uuid4

from django_project.telegrambot.usersmanage.time_model import TimeBasedModel

LANGUAGE_CHOICE = (
    (LANGUAGE_RU, "Русский"),
    (LANGUAGE_UZ, "Ўзбек"),
    (LANGUAGE_EN, "English"),
)


class User(TimeBasedModel):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    user_id = models.BigIntegerField(unique=True, default=1, verbose_name='ID Пользователя', editable=False)
    name = models.CharField(max_length=100, verbose_name='Имя пользователя', null=True)
    username = models.CharField(max_length=100, verbose_name='Username Телеграм', null=True, blank=True)
    language = models.CharField(max_length=2, default=LANGUAGE_RU, choices=LANGUAGE_CHOICE, verbose_name='Язык')
    access = models.BooleanField(verbose_name='Доступ', default=False)

    def __str__(self):
        return f"{self.user_id} - {self.name}"
