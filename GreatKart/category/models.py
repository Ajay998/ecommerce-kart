from django.db import models

# Create a Category model for ecommerce website with (category_name, slug, description, cat_image 
# with verbose name as category and data __str__ is category _name

class Category(models.Model):
    category_name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(max_length=100,unique=True)
    description = models.CharField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to="photos/categories",blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.category_name

