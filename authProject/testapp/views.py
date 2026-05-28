from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from testapp.forms import SignUpForm

# Create your business logic / views here 👇.


# Home View
def home_view(request):
    return render(request, 'testapp/home.html')

# Python View
@login_required
def python_view(request):
    print('='*35)
    print(request.user.is_authenticated)
    print('='*35)
    return render(request, 'testapp/python_exam.html')


# java View
@login_required
def java_view(request):
    return render(request, 'testapp/java_exam.html')


# Aptitude View
@login_required
def aptitude_view(request):
    return render(request, 'testapp/aptitude_exam.html')


# Sajjad View
def sajjad_view(request):
    return render(request, 'testapp/sajjad_about.html')

# Signup View
def signup_view(request):

    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return redirect('home')

    return render(request, 'registration/signup.html', {'form': form})


# Logout View 
def logout_view(request):
    logout(request)  # one user logout the session should be clear
    return render(request,'testapp/logout.html')

