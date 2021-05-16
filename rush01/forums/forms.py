from django.forms import ModelForm
from .models import *
 
class CreateInForum(ModelForm):
    class Meta:
        model= forum
        # fields = "__all__"
        fields = ['topic', 'description']


class CreateInDiscussion(ModelForm):
    class Meta:
        model= Discussion
        fields = "__all__"