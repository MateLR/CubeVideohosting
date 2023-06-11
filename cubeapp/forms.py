from django import forms
from django.core.validators import FileExtensionValidator
from .models import Comment, Video
from .validators import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class UploadVideoForm(forms.Form):
    title = forms.CharField(label='Название', max_length=20,
                            widget=forms.TextInput(attrs={'placeholder': 'Название'}), required=True)
    image = forms.ImageField(label='Превью',
                             required=True, validators=[validate_image, validate_file_size])
    video = forms.FileField(label='Видео',required=True,validators=[validate_video, validate_file_size])
    description = forms.CharField(label='Описание', max_length=300,
                                  widget=forms.TextInput(attrs={'placeholder': 'Описание'}), required=True)

# class UploadVideoForm(forms.ModelForm):
#     title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите название'}))
#     description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите описание'}))
#     image = forms.ImageField()
#
#     class Meta:
#         model = Video
#         fields = ('title', 'description', 'image')
