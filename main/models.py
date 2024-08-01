from django.db import models
from audioop import reverse
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()


class Recording_Time(models.Model):
    # name = models.CharField(max_length=100, verbose_name="Имя")
    # phone = models.CharField(max_length=15, verbose_name="Телефон")
    avto = models.CharField(max_length=100, verbose_name="Автомобиль", blank=True)
    pub_date = models.DateTimeField(verbose_name="Дата")
    time_create = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0, verbose_name="число записей", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return '{}- {}'.format(self.pk, self.avto)

    class Meta:
        verbose_name = 'Время записи клиентов'
        verbose_name_plural = 'Время записи клиентов'


class Time(models.Model):  # auto_now=False, auto_now_add=False,
    time_all = models.CharField(max_length=5, verbose_name="Время")

    def __str__(self):
        return self.time_all

    class Meta:
        ordering = ['time_all']
        verbose_name = 'Временной интервал клиентов'
        verbose_name_plural = 'Временной интервал клиентов'


class UserMessage(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email', blank=True)
    phone = models.CharField(max_length=15, verbose_name='Телефон', blank=True)
    message = models.TextField(verbose_name='Сообщение')
    is_read = models.BooleanField(default=False, verbose_name="Статус")
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_updated = models.DateTimeField(auto_now=True, verbose_name="Время прочтения")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mess', kwargs={'mess_id': self.pk})

    class Meta:
        verbose_name = 'Сообщения'
        verbose_name_plural = 'Сообщения'


class Page(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название страницы")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    body = models.TextField(verbose_name="Контент")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страницу'
        verbose_name_plural = 'Страницы'
