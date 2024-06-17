from django import forms
from .models import Item

INPUT_CLASSES = 'auth_inputs'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
            'category',
            'name',
            'description',
            'stock',
            'price',
            'sizes',
            'image',
        )
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Category'
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Item Name'
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Item Description'
            }),
            'stock': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Items available'
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Item Price'
            }),
            'sizes': forms.Select(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Item Sizes'
            }),
            'image': forms.FileInput(attrs={
                'class': 'sign_up-img',
                'placeholder': 'Item Picture'
            })
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
            'name',
            'description',
            'stock',
            'price',
            'discount',
            'sizes',
            'image',
        )

        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Item Name'
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Item Description'
            }),
            'stock': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Items available'
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Item Price'
            }),
            'discount': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Item Discount'
            }),
            'sizes': forms.Select(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Item Sizes'
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Item Picture'
            })
        }