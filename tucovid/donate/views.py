from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import *
import datetime
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        donate_history = Donate.objects.all()
        return render(request, 'index.html', {'donate_history':donate_history})
    else:
        return redirect('donate:check_user_exists')

@login_required
def home(request):
    profile = Profile.objects.filter(user=request.user)
    if not profile.exists():
        return redirect('donate:profile')

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
            return redirect('donate:profile')
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
            
            return render(request, 'settings_up.html', {'data':data})
    else:
        profile = Profile.objects.filter(user=request.user)
        data = dict()
        if profile.exists():
            data['profile'] = Profile.objects.get(user=request.user)
        else:
            data['profile'] = ''
        
        data['nav'] = ({
            '0': [
                {
                    'page':"ประวัติส่วนตัว",
                    'url':reverse('donate:profile')
                }
            ]
        })
        return render(request, 'settings_up.html', {'data':data})

@login_required
def donate(request):
    profile = Profile.objects.filter(user=request.user)
    if not profile.exists():
        return redirect('donate:profile')

    donator = Profile.objects.get(user__id=request.user.pk)
    if request.method == 'POST':
        post_copy = request.POST.copy()
        post_copy['donator'] = donator
        form = DonateForm(post_copy)
        if form.is_valid():
            form.save()
            return redirect('donate:donate')
    else:
        data = dict()
        data['items'] = DonateItem.objects.filter(show_item=True)
        data['donate'] = Donate.objects.filter(donator=donator).order_by('-id')
        data['nav'] = ({
            '0': [
                {
                    'page':"บริจาค",
                    'url':reverse('donate:donate')
                }
            ]
        })
        data['profile'] = donator
        return render(request, 'donate.html', {'data':data})

@login_required
def request(request):
    profile = Profile.objects.filter(user=request.user)
    if not profile.exists():
        return redirect('donate:profile')

    receiver = Profile.objects.get(user__id=request.user.pk)
    if request.method == 'POST':
        post_copy = request.POST.copy()
        post_copy['receiver'] = receiver
        form = ReceiveForm(post_copy)
        jobs = Job.objects.all()
        if form.is_valid():
            form.save()
            return redirect('donate:request')
    else:
        data = dict()
        data['items'] = Item.objects.all()
        data['receive'] = Receive.objects.filter(receiver=receiver).order_by('-id')
        data['nav'] = ({
            '0': [
                {
                    'page':"ขอรับบริจาค",
                    'url':reverse('donate:request')
                }
            ]
        })
        data['jobs'] = Job.objects.all()
        data['profile'] = receiver
        data['hospitals'] = Hospital.objects.all()
        return render(request, 'request.html', {'data':data})

@login_required
def printing(request):
    profile = Profile.objects.filter(user=request.user)
    if not profile.exists():
        return redirect('donate:profile')

    order = Order.objects.all().last()
    order_items = OrderItem.objects.filter(order=order)
    page = request.GET.get('page', 1)
    paginator = Paginator(order_items, 8)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    return render(request, 'printing.html', {'items':items})

@login_required
def process(request, id):
    profile = Profile.objects.filter(user=request.user)
    if not profile.exists():
        return redirect('donate:profile')
        
    if request.user.is_staff or request.user.is_superuser:
        print('Admin/Staff')
        data = dict()
        order_item = OrderItem.objects.get(pk=id)
        data['receive'] = Receive.objects.get(pk=order_item.receive.pk)
        if data['receive'].status == 'กำลังจัดส่ง':
            data['message'] = 'ทำรายการซ้ำ'
        else:
            data['receive'].status = 'กำลังจัดส่ง'
            data['receive'].save()
            data['message'] = 'Success'
        
        order = Order.objects.all().last()
        data['count'] = OrderItem.objects.filter(order=order, receive__status='กำลังจัดส่ง').count()
        print(data['count'])
        return render(request, 'alert.html', {'data':data})
    else:
        print('User')
        order_item = OrderItem.objects.get(pk=id)
        receive = Receive.objects.get(pk=order_item.receive.pk)
        receive.status='ยืนยันการรับของ'
        receive.save()
        return redirect('donate:review', id=id)

@login_required
def review(request, id):
    profile = Profile.objects.filter(user=request.user)
    if not profile.exists():
        return redirect('donate:profile')

    reviewer = Profile.objects.get(user__id=request.user.pk)
    if request.method == 'POST':
        reviews = Review.objects.filter(receive__pk=request.POST['receive'])
        if reviews.exists():
            review = Review.objects.get(receive__pk=request.POST['receive'])
            review.reviewer = reviewer
            review.score = request.POST['score']
            review.comment = request.POST['comment']
            review.save()
        else:
            post_copy = request.POST.copy()
            post_copy['reviewer'] = reviewer
            form = ReviewForm(post_copy)
            if form.is_valid():
                form.save()
        return redirect('donate:review', id=id)
    else:
        data = dict()
        order_item = OrderItem.objects.get(pk=id)
        data['id'] = id
        data['receive'] = Receive.objects.get(pk=order_item.receive.pk)
        return render(request, 'review.html', {'data':data})