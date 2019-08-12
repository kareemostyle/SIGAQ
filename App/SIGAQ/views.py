from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'SIGAQ/index.html')

def blog(request):
    return render(request, 'SIGAQ/blog.html')

def contact(request):
    return render(request, 'SIGAQ/contact.html')

def faq(request):
    return render(request, 'SIGAQ/faq.html')

def forum(request):
    return render(request, 'SIGAQ/forum.html')

def login(request):
    return render(request, 'SIGAQ/login.html')