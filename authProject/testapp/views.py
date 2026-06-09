from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
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


# Login View
def login_view(request):
    if request.method == 'POST':
        u_name = request.POST.get('username')
        p_word = request.POST.get('password')
        user = authenticate(request, username=u_name, password=p_word)
        if user is not None:
            login(request, user)
            return redirect('home')  # Login hone ke baad Home page par bhejein
        else:
            # Agar credentials galat hain
            return render(request, 'registration/login.html', {'error': 'Invalid username or password'})

    return render(request, 'registration/login.html')


# Signup / Registration View
def signup_view(request):

    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save() # Form automatically password hash kar deta hai
            login(request, user) # Signup hote hi user ko auto-login karwane ke liye
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})


# Logout View 
def logout_view(request):
    logout(request)  # one user logout the session should be clear
    return render(request,'testapp/logout.html')

