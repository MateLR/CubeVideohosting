from django.db import models
from django.core.validators import FileExtensionValidator
from users.models import User
from django.urls import reverse
from django.utils.timezone import now
from .validators import *


class Video(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=40, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images/', verbose_name='Превью',
                              validators=[validate_image, validate_file_size])
    file = models.FileField(upload_to='video/', validators=[validate_video, validate_file_size],
                            verbose_name='Видеофайл')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    likes = models.ManyToManyField(User, related_name="likes", blank=True)
    dislikes = models.ManyToManyField(User, related_name="dislikes", blank=True)
    viewed = models.ManyToManyField(User, related_name="views", blank=True)
    # url = models.URLField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view', kwargs={'pk': self.id})

    def get_view_count(self):
        return self.views.count()


class Comment(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    text = models.TextField(verbose_name='Описание', max_length=100, null=False)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=False)
    create_at = models.DateTimeField(default=now, verbose_name='Дата публикации')

    def __str__(self):
        return self.username.username + self.text


class ViewCount(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='views')
    ip_address = models.GenericIPAddressField(verbose_name='IP адрес')
    viewed_on = models.DateTimeField(auto_now_add=True, verbose_name='Дата просмотра')

    class Meta:
        ordering = ('-viewed_on',)
        indexes = [models.Index(fields=['-viewed_on'])]
        verbose_name = 'Просмотр'
        verbose_name_plural = 'Просмотры'

    def __str__(self):
        return self.video.title
