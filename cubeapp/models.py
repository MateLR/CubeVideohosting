from django.db import models
from django.core.validators import FileExtensionValidator


class Video(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(upload_to='image/')
    file = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
