from django import forms

class InputText(forms.Form):
    post_text = forms.CharField(label='input text', max_length=100, required=True)