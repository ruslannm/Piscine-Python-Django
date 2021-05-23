from django.forms import ModelForm
from .models import P

class ArticleForm(ModelForm):
    class Meta:
        model = ArticleModel
        fields = ['title', 'author', 'created', 'synopsis']
