from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as user_views

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(template_name='main/login.html', authentication_form=LoginForm), name='login'),
    path('login/', user_views.CustomLoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('profile/<str:username>/', user_views.profile, name='profile'),
    path('profile_update/', user_views.profile_update, name='profile_update'),
    path('signup/', user_views.signup, name='signup'),
]