from django.db import models
from django.contrib.auth.models import User
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from secrets import token_urlsafe


# Create your models here.
class Urlentry(models.Model):
    owner = models.ForeignKey(User, verbose_name='Владелец', on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    full_url = models.URLField('Полная ссылка', unique=True)
    url_hash = models.URLField('Короткая ссылка', unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            while True:
                self.url_hash = token_urlsafe(nbytes=4)
                if not Urlentry.objects.filter(url_hash=self.url_hash):
                    break
        validate = URLValidator()
        try:
            validate(self.full_url)
        except ValidationError as e:
            raise 'invalid url'
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.url_hash

    class Meta:
        verbose_name_plural = "Ссылки"


class Leads(models.Model):
    urlentry = models.ForeignKey(Urlentry, verbose_name='Короткая ссылка', on_delete=models.CASCADE)
    clicked_at = models.DateTimeField('Дата и время перехода по ссылке', auto_now_add=True)
    clicked_host = models.TextField('Откуда перешли')
    clicked_conf = models.TextField('Конфигурация устройства пользователя')
    clicked_ip = models.TextField('IP-адрес')
    def __str__(self):
        return self.clicked_at

    class Meta:
        verbose_name_plural = "Переходы"
