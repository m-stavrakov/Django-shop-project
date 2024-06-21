from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('', views.items_search, name='items_search'),
    path('category/<int:category_id>/', views.category_items, name='category-items'),
    path('new/', views.new_item, name='new_item'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete_item, name='delete'),
    path('<int:pk>/edit/', views.edit_item, name='edit'),
]