from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from .forms import *
import datetime
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return render(request, 'index.html')
    else:
        return redirect('donate:check_user_exists')

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def verify_user(request):
    profile = Profile.objects.filter(user=request.user)
    if profile.exists():
        return redirect('donate:home')
    else:
        return redirect('donate:profile')

@login_required
def profile(request):
    if request.method == 'POST':
        post_copy = request.POST.copy()
        post_copy['user'] = request.user.pk
        print(post_copy)
        profile = Profile.objects.filter(user=request.user)
        if profile.exists():
            form = ProfileForm(post_copy, instance=Profile.objects.get(user=request.user))
        else:
            form = ProfileForm(post_copy)

        if form.is_valid():
            form.save()
            return redirect('donate:home')
        else:
            data = dict()
            data['nav'] = ({
            '0': [
                    {
                        'page':"ประวัติส่วนตัว",
                        'url':reverse('donate:profile')
                    }
                ]
            })
            jobs = Job.objects.all()
            return render(request, 'settings_up.html', {'data':data,'jobs':jobs})
    else:
        profile = Profile.objects.filter(user=request.user)
        data = dict()
        if profile.exists():
            data['profile'] = Profile.objects.get(user=request.user)
        else:
            data['profile'] = ''
        jobs = Job.objects.all()
        data['nav'] = ({
            '0': [
                {
                    'page':"ประวัติส่วนตัว",
                    'url':reverse('donate:profile')
                }
            ]
        })
        return render(request, 'settings_up.html', {'data':data, 'jobs':jobs})

@login_required
def donate_history(request):
    data = Donate.objects.filter(created_by=request.user)
    return render(request, 'donate_history.html', {'data':data})

@login_required
def donate(request):
    if request.method == 'POST':
        post_copy = request.POST.copy()
        post_copy['created_by'] = request.user.pk
        form = DonateForm(post_copy)
        if form.is_valid():
            form.save()
            return redirect('donate:donate')
    else:
        items = DonateItem.objects.all()
        data = dict()
        data['donate'] = Donate.objects.filter(created_by=request.user).order_by('-id')
        data['nav'] = ({
            '0': [
                {
                    'page':"บริจาค",
                    'url':reverse('donate:donate')
                }
            ]
        })
        return render(request, 'donate.html', {'items':items, 'data':data})

@login_required
def request_history(request):
    data = Receive.objects.filter(created_by=request.user)
    return render(request, 'request_history.html', {'data':data})

@login_required
def request(request):
    if request.method == 'POST':
        post_copy = request.POST.copy()
        post_copy['created_by'] = request.user.pk
        form = ReceiveForm(post_copy)
        if form.is_valid():
            print('aaaaaaaaaaaaaaaaaaaaaaaaaaaa')
            form.save()
            return redirect('donate:request')
        else:
            print('-----------------form valid----------------')
            print(form)
    else:
        items = Item.objects.all()
        data = dict()
        data['receive'] = Receive.objects.filter(created_by=request.user).order_by('-id')
        data['nav'] = ({
            '0': [
                {
                    'page':"ขอรับบริจาค",
                    'url':reverse('donate:request')
                }
            ]
        })
        return render(request, 'request.html', {'items':items, 'data':data})

@login_required
def review(request):
    return render(request, 'review.html')