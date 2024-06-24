from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as user_views
from .views import UserProfileView

app_name = 'user'

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('profile/<str:username>/', user_views.profile, name='profile'),
    path('profile/<str:username>/', UserProfileView.as_view(), name='user_profile'),
    path('profile_update/', user_views.profile_update, name='profile_update'),
    path('signup/', user_views.signup, name='signup'),
]