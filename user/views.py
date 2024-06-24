from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import SignupForm, UserUpdateForm,ProfileUpdateForm, LoginForm
from item.models import Category, Item
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.views.generic import DetailView
import logging

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save()
            profile_picture = form.cleaned_data.get('profile_picture')
            if profile_picture:
                profile = user.profile
                profile.profile_img = profile_picture
                profile.save()
            
            messages.success(request, f'Account created for {user.username}!')
            login(request, user)
            return redirect('main:home_page')
    else:
        form = SignupForm()
    
    return render(request, 'user/signup.html', {
        'form': form,
    })

# changes
logger = logging.getLogger(__name__)
class CustomLoginView(LoginView):
    template_name = 'user/login.html'
    authentication_form = LoginForm

    # changes
    def form_invalid(self, form):
        logger.error('Login form invalid: %s', form.errors)
        return super().form_invalid(form)
    
    def form_valid(self, form):
        try:
            user = form.get_user()
            messages.success(self.request, f'Welcome {user.first_name}! You have successfully logged in!')
            return super().form_valid(form)
        except Exception as e:
            logger.error('Error during form validation: %s', str(e))
            messages.error(self.request, 'An unexpected error occurred. Please try again later.')
            return self.form_invalid(form)

    # def form_valid(self, form):
    #     user = form.get_user()
    #     messages.success(self.request, f'Welcome {user.first_name}! You have successfully logged in!')
    #     return super().form_valid(form)

@login_required
def profile(request, username):
    user_profile = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user_profile)
    profile_image = profile.profile_img.url
    user_items = Item.objects.filter(created_by=user_profile, is_sold=False)[:6]
    categories = Category.objects.all()

    return render(request, 'user/profile.html', {
        'profile_image': profile_image,
        'user_items': user_items,
        'categories': categories,
        'current_user': request.user,
        'user_profile': user_profile,
        'profile': profile,
    })

@login_required
def profile_update(request):
    # Handling profile updates
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, 
                                         request.FILES, 
                                         instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile', username=request.user.username)
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'user/profile_update.html', context)

class UserProfileView(DetailView):
    model = User
    template = 'profile.html'
    context_object_name = 'user_profile'

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])