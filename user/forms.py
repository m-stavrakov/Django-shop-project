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
    profile_picture = forms.ImageField(required=False, label='Profile Picture', widget=forms.ClearableFileInput(
        attrs={
            'class': 'sign_up-img'
        }
    ))

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
    password1 = forms.CharField(label='Your password', widget=forms.PasswordInput(attrs={'class': 'password-toggle auth_inputs password', 'placeholder': 'Your Password'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'password-toggle auth_inputs password', 'placeholder': 'Confirm Password'}))

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name == 'profile_picture':
                field.widget.attrs.update({
                    'class': 'form-control sign_up-img',
                })
            else:
                field.widget.attrs.pop('autofocus', None)
                field.widget.attrs.update({
                    'class': 'form-control password auth_inputs',
                })

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
    
    first_name = custom_char_field('Your First Name')
    last_name = custom_char_field('Your Last Name')
    username = custom_char_field('Your username')
    email = custom_char_field('Your email address')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_img']
    
    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['profile_img'].widget.attrs.update({'class': 'sign_up-img'})

class LoginForm(AuthenticationForm):
    username = custom_char_field('Your username')
    password = forms.CharField(label='Your password', widget=forms.PasswordInput(attrs={'class': 'form-control password auth_inputs', 'placeholder': 'Your Password', 'id': 'password_login'}))

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
    
