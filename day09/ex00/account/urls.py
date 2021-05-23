from django.urls import path
from django.views.generic import TemplateView
from . import ajax


urlpatterns = [
    path('get_element/', ajax.get_element),
    path('', TemplateView.as_view(template_name='account/account.html')),
]
