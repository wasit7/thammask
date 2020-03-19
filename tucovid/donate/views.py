from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from .forms import *
import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')
def verify_user(request):
    profile = Profile.objects.filter(user=request.user)
    if profile.exists():
        return redirect('donate:donate_history')
    else:
        return redirect('donate:profile')

def profile(request):
    if request.method == 'POST':
        post_copy = request.POST.copy()
        post_copy['date_of_birth'] = datetime.datetime.strptime(request.POST['date_of_birth'], "%d %B %Y")
        post_copy['user'] = request.user.pk
        print(post_copy)
        profile = Profile.objects.filter(user=request.user)
        if profile.exists():
            form = ProfileForm(post_copy, instance=Profile.objects.get(user=request.user))
        else:
            form = ProfileForm(post_copy)
        if form.is_valid():
            form.save()
            return redirect('donate:donate_history')
        else:
            return render(request, 'settings_up.html')
    else:
        profile = Profile.objects.filter(user=request.user)
        if profile.exists():
            data = Profile.objects.get(user=request.user)
        else:
            data = ''
        return render(request, 'settings_up.html', {'data':data})

def donate_history(request):
    data = Donate.objects.filter(created_by=request.user)
    return render(request, 'donate_history.html', {'data':data})

def donate(request):
    if request.method == 'POST':
        post_copy = request.POST.copy()
        post_copy['created_by'] = request.user.pk
        form = DonateForm(post_copy)
        if form.is_valid():
            form.save()
            return redirect('donate:donate_history')
    else:
        items = Item.objects.all()
        return render(request, 'donate.html', {'items':items})

def request_history(request):
    data = Receive.objects.filter(created_by=request.user)
    return render(request, 'request_history.html', {'data':data})

def request(request):
    if request.method == 'POST':
        post_copy = request.POST.copy()
        post_copy['created_by'] = request.user.pk
        form = ReceiveForm(post_copy)
        if form.is_valid():
            form.save()
            return redirect('donate:request_history')
    else:
        items = Item.objects.all()
        return render(request, 'request.html', {'items':items})

def review(request):
    return render(request, 'review.html')