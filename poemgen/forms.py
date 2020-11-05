from django import forms
from .models import Word
from django.shortcuts import render
from django.http import HttpResponseRedirect

class PoemGenForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = [
            "input_word"
        ]

    def word_saving(request):
        if request.method == "POST":
            form = PoemGenForm(request.POST)
            if form.is_valid():
                input_words = form.cleaned_data
            #else
            return render(request, '/yourpoem.html', '')
    
    #def generate(self): ide kerül a szöveg generálás