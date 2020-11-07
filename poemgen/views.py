from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Poem, PoemDetails
from .forms import PoemModelForm
from .generator import *

def home(request):
    poems = Poem.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'poemgen/home.html', {'poems':poems})

texts =[
    {
        'title': 'Az appról',
        'content': ' Szakdolgozatom célja, olyan versgenerátor szoftver elkészítése, amely a magyar nyelvű generáláson kívül különböző szempontoknak is megfelel, mint a kulcsszavak szerinti generálás, különböző művészek stílusának átemelése - stílusnak való megfelelés, mondatonként - szakaszonként egybefüggő nyelvezet.'
    },
    {
        'title': 'Hogyan generálj?',
        'content':' A generátor fülre kattintva, csupán egyetlen szó beírásával párszavas verset kapsz, vezetett útmutatás vár az oldalon. Amennyiben az általad beírt szó szerepel az adatbázisban láthatod az eredményt, ellenkező esetben ...'
    },
    {
        'title': 'Lehetőségek',
        'content': 'Továbbfejlesztési lehetőségnek említeném: A markov-lánccal való generálást helyettesíthetnénk MI által generálással, a szövegek hosszának és tördelésének módosításával rímképlet szerinti generálást is meg lehetne valósítani.'
    }
]

def about(request):
    context = {
        'texts': texts
    }
    return render(request, 'poemgen/about.html', context)

def yourpoem(request):
    return render(request, 'poemgen/yourpoem.html')

def generator(request):

    if request.method == 'POST':
        form = PoemModelForm(request.POST)
        if form.is_valid():

            p = form.save()
            poems = PoemDetails.objects.all()

            return render(request, 'poemgen/yourpoem.html', {'poems': poems})

    else:
        form_class = PoemModelForm

    return render(request, 'poemgen/generator.html', {
        'form': form_class,
    })