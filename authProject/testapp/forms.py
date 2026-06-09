from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
    
    class Meta:
        model = User
        fields = ['username', 'password'] # Jo fields aapko chahiye
        
        # Username field me bhi bootstrap class jodne ke liye widgets block:
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}),
        }