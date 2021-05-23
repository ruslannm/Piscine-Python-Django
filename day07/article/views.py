from .models import Article
from django.views.generic import ListView


class HomeView(ListView):
    model = Article
    template_name = "article/articles.html"
