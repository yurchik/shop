from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=60, blank=True, null=True, default=None)
    parent_id = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "Категория: {}".format(self.name)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    category = models.ForeignKey(Category, blank=True, null=True, default=None)
    discount = models.IntegerField(default=0)
    short_description = models.TextField(blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2)        # price * nmb
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='/product_images/')
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Фотография: {}".format(self.id)

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"
