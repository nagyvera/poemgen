from django import forms
from .models import Poem

class PoemGenForm(forms.ModelForm):
    class Meta:
        model = Poem
        fields = [
            "title"
        ]