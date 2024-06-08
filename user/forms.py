from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from .models import Profile

def custom_char_field(placeholder):
    return forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': placeholder,
        'class': ''
    }))

class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        )

    first_name = custom_char_field('Your First Name')
    last_name = custom_char_field('Your Last Name')
    username = custom_char_field('Your username')
    email = custom_char_field('Your email address')
    password1 = custom_char_field('Your password')
    password2 = custom_char_field('Confirm password')

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
        ]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_img']

class LoginForm(AuthenticationForm):
    username = custom_char_field('Your username')
    password = custom_char_field('Your password')

    # Allowing user to log in with either username or email
    def clean(self):
        username_or_email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username_or_email and password:
            if '@' in username_or_email:
                try:
                    user = User.objects.get(email=username_or_email)
                    username = user.username
                except User.DoesNotExist:
                    raise ValidationError('Invalid email or password')
            else:
                username = username_or_email
            
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise ValidationError('Invalid username/email or password')
            else:
                self.confirm_login_allowed(self.user_cache)
            
        return self.cleaned_data