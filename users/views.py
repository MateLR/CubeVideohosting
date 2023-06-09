from django.shortcuts import render, HttpResponseRedirect
from .models import User
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib import auth, messages
from django.urls import reverse
from cubeapp.models import Video


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/registration.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def customer(request, pk):
    user = User.objects.get(id=pk)
    context = {
        'customer': User.objects.get(id=pk),
        'videos': Video.objects.filter(username=user)
    }
    return render(request, 'users/customer.html', context)
