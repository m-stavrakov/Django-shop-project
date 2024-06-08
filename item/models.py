from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils.text import slugify
from django.core.exceptions import ValidationError

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        ordering = ('name', )
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

SIZE_CHOICES = (
    ('sm', 'Small'),
    ('md', 'Medium'),
    ('lg', 'Large'),
    ('xl', 'Extra Large'),
    ('2xl', 'Double Extra Large'),
)

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    stock = models.PositiveIntegerField(default=0)
    discount = models.FloatField(default=0.0)
    sizes = models.CharField(max_length=3, choices=SIZE_CHOICES, default='sm')

    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    # for better search in the database
    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['price']),
        ]

    def __str__(self):
        return f"{self.name} ({self.category.name})"   
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        self.resize_image()

    def resize_image(self):
        if self.image:
            img = Image.open(self.image.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)
    
    def get_final_price(self):
        return self.price * (1 - self.discount / 100)
    
    def clean(self):
        if self.price < 0:
            raise ValidationError('Price cannot be negative')
        
        if self.stock < 0:
            raise ValidationError('Stock amount cannot be negative')