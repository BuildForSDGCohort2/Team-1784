from django.shortcuts import render,get_object_or_404,redirect
from profiles.models import Donor,Grievance,RegularUser

def donorDashboard(request):
    user = request.user
    duser = get_object_or_404(Donor, user=user)
    context = {
        'title': f'{request.user} Dashboard',
        'duser': duser,
    }
    return render(request, 'dashboard/donor-dashboard.html', context)

def notification(request):
    if request.user.userType == 'Donor / organization':
        return redirect('dashboard:duser')
    context = {
        'title': f'{request.user.username} Notification'
    }
    return render(request, 'dashboard/notification.html')