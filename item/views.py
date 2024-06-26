from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Category, Item
from .forms import NewItemForm, EditItemForm

# Create your views here.
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk) [:3]
    final_price = item.get_final_price()

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items,
        'final_price': final_price
    })

def category_items(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    items = Item.objects.filter(category=category)

    return render(request, 'item/category_items.html', {
        'category': category,
        'items': items
    })

@login_required
def new_item(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            
            return redirect('item:detail', pk=item.id)
    
    else:
        form = NewItemForm()

    return render(request, 'item/item.html',{
        'form': form,
        'title': 'New Item'
    })

@login_required
def edit_item(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.pk)
        
    else:
        form = EditItemForm(instance=item)
    
    return render(request, 'item/item.html', {
        'form': form,
        'title': 'Edit Item'
    })

@login_required
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')

# items search
def items_search(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)
    
    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    return render(request, 'item/items_search.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
    })