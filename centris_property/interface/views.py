from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Centris

# Create your views here.


def index(request):
    centris = Centris.objects.all()
    # paginator = Paginator(centris, 15)
    # page = request.GET.get('page')
    #
    # centris = paginator.get_page(page)
    context = {
        'centris': centris
    }

    return render(request, 'interface/index.html', {'centris': centris})

# def search(request):
#