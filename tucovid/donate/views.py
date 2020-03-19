from django.shortcuts import render, redirect, HttpResponse
from .forms import *
import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def profile(request):
    if request.method == 'POST':
        post_copy = request.POST.copy()
        post_copy['date_of_birth'] = datetime.datetime.strptime(request.POST['date_of_birth'], "%d %B %Y")
        form = ProfileForm(post_copy)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donate_history')
        else:
            return render(request, 'settings_up.html')
    else:
        return render(request, 'settings_up.html')

def donate_history(request):
    data = Donate.objects.all()
    return render(request, 'donate_history.html', {'data':data})

def donate(request):
    if request.method == 'POST':
        form = DonateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donate_history')
    else:
        items = Item.objects.all()
        return render(request, 'donate.html', {'items':items})

def request_history(request):
    data = Receive.objects.all()
    return render(request, 'request_history.html', {'data':data})

def request(request):
    if request.method == 'POST':
        form = ReceiveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('request_history')
    else:
        items = Item.objects.all()
        return render(request, 'request.html', {'items':items})

def review(request):
    return render(request, 'review.html')