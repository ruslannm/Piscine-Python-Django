from django.forms import ModelForm
from .models import *
from django import forms

class CreateInForum(ModelForm):
    class Meta:
        model= forum
        # fields = "__all__"
        fields = ['topic', 'description']


class CreateInDiscussion(ModelForm):
#    forum = models.ForeignKey(forum , on_delete=models.CASCADE, editable=False)
#    readonly_fields = ('forum',)
    
    class Meta:
        model= Discussion
        fields = ['forum', 'discuss', ]

    
    # def __init__(self, *args, **kwargs):
    #     super(CreateInDiscussion, self).__init__(*args, **kwargs)
    #     for field in self.readonly_fields:
    #         self.fields[field].disabled = True