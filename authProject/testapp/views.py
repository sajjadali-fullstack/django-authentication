from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your business logic / views here.

# Home View
def home_view(request):
    return render(request, 'testapp/home.html')

# Python View
def python_view(request):
    return render(request, 'testapp/python_exam.html')

# java View
def java_view(request):
    return render(request, 'testapp/java_exam.html')

# Aptitude View
def aptitude_view(request):
    return render(request, 'testapp/aptitude_exam.html')

# Sajjad View
def sajjad_view(request):
    return render(request, 'testapp/sajjad_about.html')