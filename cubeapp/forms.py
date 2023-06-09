from django import forms
from django.core.validators import FileExtensionValidator
from .models import Comment, Video


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class UploadVideoForm(forms.Form):
    title = forms.CharField(label='Название', max_length=20,
                            widget=forms.TextInput(attrs={'placeholder': 'Описание'}), required=False)
    image = forms.ImageField(label='Превью', validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg'])],
                             required=False)
    description = forms.CharField(label='Описание', max_length=300,
                                  widget=forms.TextInput(attrs={'placeholder': 'Описание'}), required=False)
