from django.contrib import admin
from .models import Poem, PoemDetails

# Register your models here.
admin.site.register(Poem)
admin.site.register(PoemDetails)