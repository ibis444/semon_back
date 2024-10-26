from django.db import models

from django.urls import reverse

class HeroSection(models.Model):
    image = models.ImageField(upload_to='hero_sections/')
    
class AboutHomePage(models.Model):
    image = models.ImageField(upload_to='about_home/')
    title = models.CharField(max_length=200) 
    description = models.TextField()    
    def __str__(self):
        return self.title 
    
class ProductHomePage(models.Model):
    image = models.ImageField(upload_to='products/')  
    title = models.CharField(max_length=120)          
    description = models.TextField()                   
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    
    

    def __str__(self):
        return self.title
    

class ProjectHomePage(models.Model):
    image = models.ImageField(upload_to='project/')  
    title = models.CharField(max_length=120)          
    
    
    

    def __str__(self):
        return self.title
    

class Statistic(models.Model):
    image = models.ImageField(upload_to='statistics/')  
    count = models.IntegerField() 
    description = models.CharField(max_length=100)  

    def __str__(self):
        return self.description
    
class Partners(models.Model):
    image = models.ImageField(upload_to='partners/')  
    
    
# ______________________________________________________________________________________

class AboutUs(models.Model):
    image_1 = models.ImageField(upload_to='about/')
    title_1 = models.CharField(max_length=120)
    description_1 = models.TextField()

    image_2 = models.ImageField(upload_to='about/')
    title_2 = models.CharField(max_length=120)
    description_2 = models.TextField()

    def __str__(self):
        return self.title_1
    
class Certificate(models.Model):
    image = models.ImageField(upload_to='cert/')  
    
# ______________________________________________________________________________________
class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField(max_length=30)
    subject=models.CharField(max_length=35)
    message=models.TextField()  
    def __str__(self):
        return self.name  

