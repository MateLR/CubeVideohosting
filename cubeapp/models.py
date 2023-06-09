from django.db import models
from django.core.validators import FileExtensionValidator


# class Video(models.Model):
#     username = models.ForeignKey('User', on_delete=models.CASCADE, null=False)
#     title = models.CharField(max_length=40, verbose_name='Название')
#     description = models.TextField(verbose_name='Описание')
#     image = models.ImageField(upload_to='image/', verbose_name='Превью')
#     file = models.FileField(upload_to='video/', validators=[FileExtensionValidator(allowed_extensions=['mp4'])],
#                             verbose_name='Видеофайл')
#     create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
#     url = models.URLField(unique=True)
#
#     def __str__(self):
#         return self.title
