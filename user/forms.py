from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from .models import Profile

def custom_char_field(placeholder, input_type='text', **kwargs):
    attrs = {
        'placeholder': placeholder,
        'class': 'auth_inputs',
    }
    attrs.update(kwargs)
    
    widget = forms.TextInput(attrs=attrs)
    if input_type == 'password':
        widget = forms.PasswordInput(attrs=attrs)
    
    return forms.CharField(widget=widget)

class SignupForm(UserCreationForm):
    email = forms.EmailField()
    profile_picture = forms.ImageField(required=False, label='Profile Picture')

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
            'profile_picture',
        )

    first_name = custom_char_field('Your First Name')
    last_name = custom_char_field('Your Last Name')
    username = custom_char_field('Your username')
    email = custom_char_field('Your email address')
    password1 = custom_char_field('Your password', input_type='password', id='password1')
    password2 = custom_char_field('Confirm password', input_type='password', id='password2')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.pop('autofocus', None)

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
    password = custom_char_field('Your password', input_type='password', id='password_login')

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