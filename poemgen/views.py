from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Poem, PoemDetails
from .forms import PoemModelForm
from .generator import *

def poem_list(request):
    poems = Poem.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'poemgen/poem_list.html', {'poems':poems})

posts = [
    {
        'title': 'Első vers - megadott szó: haza',
        'content': 'haza vágyom. Összebuvó félelem homályával nagyranyilt szemük',
        'date_posted': '2020-09-20'
    },
    {
        'title': 'Második vers - megadott szó: magam',
        'content': ' magam búsultató dolga volt ő: embernyi , sárga irka ',
        'date_posted': '2020-09-21'
    },
    {
        'title': 'Harmadik vers - megadott szó: harc',
        'content': ' harc nagy szégyeneiért , rabmadaracskám ! meghalok s társadtól jön a gyér fűből bő harmat gördül ',
        'date_posted': '2020-10-07'
    },
    {
        'title': 'Negyedik vers - megadott szó: harc',
        'content': ' Harc ez - Bocsáss, fölsikálja a fizetséged ? Gyengék vagyunk; szenet árul , fölsikálja a fizetséged ',
        'date_posted': '2020-10-07'
    },
    {
        'title': 'Ötödik vers - megadott szó: harc',
        'content': ' Harc ez kijárt neki . Március. A tőkések hasznáról Dagassz gázlángnál kenyeret, amiket a gangon',
        'date_posted': '2020-10-07'
    },
    {
        'title': 'Hatodik vers - megadott szó: virág',
        'content': ' virág , ha nem hagytuk volna ott terem gyönyörűszép szívemen el - Ellenség ha tör borsot ',
        'date_posted': '2020-10-17'
    }

]

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

def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'poemgen/home.html', context)

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