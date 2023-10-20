from django.shortcuts import render
from .models import Naat

def naat(request):
    if request.method == 'POST':
        search_term = request.POST.get('search')
        matching_naats = Naat.objects.filter(tittle__icontains=search_term)
        return render(request, 'naat.html', context={'matching_naats': matching_naats})

    return render(request, 'naat.html')
