from django.shortcuts import render,redirect,get_object_or_404
from profiles.models import Grievance,RegularUser,Donor
from users.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def discoverView(request):
    grievances = Grievance.objects.all()
    user = request.user
    added = False
    context = {
        'grievances': grievances,
        'added': added,
        'title': 'Discover Africans Potentials'
    }
    return render(request, 'discover/index.html', context)

@login_required
def discoverDetail(request, id):
    # user = User.objects.get(username=regular_user)
    reguser = RegularUser.objects.get(grievance=id)
    postDetail = get_object_or_404(Grievance, id=id)
    user = request.user
    added = False
    if user.userType == 'Donor / organization':
        duser = get_object_or_404(Donor,user=user)
        if duser.selected.filter(id=reguser.id):
            added = True
            context = {
            'added': added,
            'post': postDetail,
            'title': f'{reguser.user} details',
            }
            return render(request, 'discover/detail.html', context)
    
    context = {
    'added': added,
    'post': postDetail,
    'title': f'{reguser.user} details',
    }
    return render(request, 'discover/detail.html', context)

    
@login_required
def addReqularUser(request, id):
    reguser = RegularUser.objects.get(grievance=id)
    duser = get_object_or_404(Donor, user=request.user)
    duser.selected.add(reguser)
    messages.info(request, f'{duser.user} successful added to users you want to help ')
    return redirect('discover:detail', id=id)

    
@login_required
def removeReqularUser(request, id):
    reguser = RegularUser.objects.get(grievance=id)
    duser = get_object_or_404(Donor, user=request.user)
    duser.selected.remove(reguser)
    messages.info(request, f'{duser.user} removed successful')
    return redirect('discover:detail', id=id)

@login_required
def removeRegUser(request, id):
    reguser = RegularUser.objects.get(id=id)
    duser = get_object_or_404(Donor, user=request.user)
    duser.selected.remove(reguser)
    messages.info(request, f'{duser.user} removed successful')
    return redirect('dashboard:duser')