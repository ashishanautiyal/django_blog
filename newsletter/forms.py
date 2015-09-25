__author__ = 'Ashish'

from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['email', 'full_name']
        #exclude = ['full_name']  do not use it . It only tells what not going on

