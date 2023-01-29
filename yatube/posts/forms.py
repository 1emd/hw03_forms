from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('text', 'group',)
        help_texts = {
            'text': ('Введите текст'),
            'group': ('Выберете группу'),
        }

    def clean_text(self):
        data = self.cleaned_data['text']
        if '' not in data.lower():
            raise forms.ValidationError('Вы должны написать!')
        return data
