from django.shortcuts import render, redirect
from item.models import Category, Item

# Create your views here.

def home_page(request):
    items = Item.objects.filter(is_sold=False).order_by('-created_at') [0:6]
    categories = Category.objects.all()


    return render(request, 'main/home_page.html', {
        'items': items,
        'categories': categories,
        'user': request.user,
    })