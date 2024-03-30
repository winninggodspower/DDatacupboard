from django.shortcuts import render
from .models import Data

# Create your views here.
def home(request):
    datasets = Data.objects.all()

    # filter datasets by search query if the user made a serach
    search_query = request.GET.get('q')
    if search_query:
        datasets = datasets.filter(title__icontains=search_query)

    context = {
        'datasets': datasets,
        'search_query': search_query
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')