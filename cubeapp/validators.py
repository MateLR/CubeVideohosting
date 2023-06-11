from django.core.exceptions import ValidationError


def validate_video(value):
    import os
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.mp4', '.avi']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Формат файла не поддерживается')


def validate_image(value):
    import os
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.png', '.jpg', '.jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Формат файла не поддерживается')


def validate_file_size(value):
    limit = 1000 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('Файл слишком большой')
