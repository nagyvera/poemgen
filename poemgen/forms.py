from django.forms import ModelForm, widgets
from .models import PoemDetails

class PoemModelForm(ModelForm):
    class Meta:
        model = PoemDetails
        fields = ['title']
        widgets = {
            'text': widgets.HiddenInput()
        }