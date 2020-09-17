from django.shortcuts import render,redirect
from profiles.models import Grievance


def discoverView(request):
    grievances = Grievance.objects.all()
    context = {
        'grievances': grievances,
        'title': 'Discover Africans Potentials'
    }
    return render(request, 'discover/index.html', context)