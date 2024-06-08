from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils.text import slugify

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(default='default.jpg', upload_to='profile_imgs')
    slug = models.SlugField(max_length=250, unique=True, blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} Profile'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.user.first_name} {self.user.last_name}')
            
        super().save(*args, **kwargs)

        img = Image.open(self.profile_img.path)

        if img.width > 300 or img.height > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_img.path)