from itertools import product

from django.db import models

# Create your models here.


# class Car(models.Model):
#     name = models.CharField(max_length=255)
#     color = models.CharField(max_length=10)
#     price = models.DecimalField(max_digits=14, decimal_places=2)
#
#     def __str__(self):
#         return self.name

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    parent = models.ForeignKey(
        'self',
        related_name='children',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    is_active = models.BooleanField(default=True)


    def __str__(self):
        if self.parent:
            return f"{self.parent.title} -> {self.title}"
        return self.title

    class Meta:
        verbose_name_plural = 'categories'


    @property
    def product_count(self):

        count = self.products.all().count()
        for child in self .children.filter(is_active=True):
            count+=child.product_count

        return count

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=14, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey('Category',
                                 related_name='products',
                                 on_delete=models.SET_NULL,
                                 null=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey('Product',
                                related_name='images',
                                on_delete=models.SET_NULL,
                                null=True)
    image = models.ImageField(upload_to='product/images')


    def __str__(self):
        return self.name

