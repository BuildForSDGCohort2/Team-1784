from django.shortcuts import render,redirect,get_object_or_404
from .forms import DonorForm,GrievanceForm,RegularUserForm
from .models import RegularUser,Grievance,Donor,Starred
from django.contrib.auth.decorators import login_required

@login_required
def regularUser(request):
    instance = get_object_or_404(RegularUser,  user=request.user)
    regular_form = RegularUserForm(request.POST or None, instance=instance)
    if request.method == "POST":
        if regular_form.is_valid():
            regular_form.save()
            return redirect('home:index')
           
    context = {
        'form': regular_form,
        'title': f'{request.user} profile'
    }
    return render(request, 'profiles/regularUser.html', context)

@login_required
def donorUser(request):
    instance = get_object_or_404(Donor, user=request.user)
    donor_form = DonorForm(request.POST or None, instance=instance)
    if request.method == "POST":
        if donor_form.is_valid():
            donor_form.save()
            return redirect('home:index')
    context = {
        'form': donor_form,
        'title': f'{request.user} profile',
    }
    return render(request, 'profiles/donorUser.html', context)

def grievanceView(request):
    ruser = RegularUser.objects.filter(user=request.user)
    instance = get_object_or_404(Grievance, regular_user=ruser[0])
    grievanceForm = GrievanceForm(request.POST or None,request.FILES or None , instance=instance)
    if request.method == 'POST':
        if grievanceForm.is_valid():
            grievanceForm.save()
            return redirect('home:index')
    context = {
        'form': grievanceForm,
        'title': f'{request.user} grievance post'
    }
    return render(request, 'profiles/grievancePost.html', context)


def userProfile(request):
    if request.user == 'Donor / organization':
        return redirect('profiles:duser')
    else:
        return redirect('profiles:reguser')