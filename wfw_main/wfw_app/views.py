from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def profile(request):
    return render(request, 'profile.html')


def about(request):
    return render(request, 'about.html')


def chat(request):
    return render(request, 'chat.html')


def match(request):
    return render(request, 'match.html')