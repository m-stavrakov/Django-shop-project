from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from .forms import SignupForm, UserUpdateForm,ProfileUpdateForm, LoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')

            return redirect('/login/')
    else:
        form = SignupForm()
    
    return render(request, 'user/signup.html', {
        'form': form,
    })

class CustomLoginView(LoginView):
    template_name = 'user/login.html'
    authentication_form = LoginForm

    def valid_form(self, form):
        user = form.get_user()
        messages.success(self.request, f'Welcome {user.first_name}! You have successfully logged in!')
        return super().form_valid(form)

@login_required
def profile(request):
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
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'user/profile.html', context)