from django.shortcuts import render,redirect
from users.forms import LoginForm,SignupForm
from .forms import ContactForm

def index(request):
    signupform = SignupForm(request.POST or None)
    loginform = LoginForm(request.POST or None)
    context = {
        'title': 'Africans Potentials',
        'signupform': signupform,
        'loginform': loginform,

        }
    return render(request, 'home/index.html', context)

def contact(request):
    contact_form = ContactForm(request.POST or None)
    if contact_form.is_valid():
        contact_form.save()
        return redirect('home:contact')
    context = {
        'contact_form': contact_form
    }
    return render(request, 'home/contact.html', context)
