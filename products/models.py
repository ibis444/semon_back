from django.db import models

class Product(models.Model):
    title=models.CharField(max_length=40)
    price=models.CharField(max_length=10)
    description=models.TextField() 
    def __str__(self):
        return self.title 

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images') 
    image = models.ImageField(upload_to='images')
    def get_image_display(self):
        return self.image.url 

class StaticImage(models.Model):
    image=models.ImageField(upload_to='images')
    def __str__(self):
        return self.image.name 

class BunlarBax(models.Model):
    image = models.ImageField(upload_to='bunlar/')  