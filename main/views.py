from django.shortcuts import render
from django.contrib import messages
from .models import Data, Feedback

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

def feedback(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        service_rating = request.POST.get('service_rating')
        would_recommend = request.POST.get('would_recommend')
        additional_feedback = request.POST.get('additional_feedback')
        Feedback.objects.create(
            name=name,
            email=email,
            service_rating=service_rating,
            would_recommend=would_recommend,
            additional_feedback=additional_feedback
        )
        messages.success(request, 'successfully sent a feedback. Thanks 👏')
    return render(request, 'feedback.html')