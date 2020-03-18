from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'settings_up.html')

def donate_history(request):
    return render(request, 'donate_history.html')

def donate(request):
    return render(request, 'donate.html')

def request_history(request):
    return render(request, 'request_history.html')

def request(request):
    return render(request, 'request.html')