from django.db import models

class Agent(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    image = models.FileField(upload_to='agents/' )
    desc = models.TextField()


    def __str__(self):
        return self.full_name
    
class Index(models.Model):
    index_title = models.CharField(max_length=255)
    index_text = models.TextField()
    
    def __str__(self):
        return self.index_title
    
    
class About(models.Model):
    about_title = models.CharField(max_length=255)
    about_text = models.TextField()

    def __str__(self):
        return self.about_text
        
    
class Service(models.Model):
    service_title = models.CharField(max_length=255)
    service_text = models.TextField()

    def __str__(self):
        return self.service_text
             
    
class Contact(models.Model):
    contact_title = models.CharField(max_length=255)
    contact_text = models.TextField()
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    contact_address = models.CharField(max_length=255)


    def __str__(self):
        return self.contact_text
        
class Properties(models.Model):
    property_title = models.CharField(max_length=255)
    property_text = models.TextField()
    property_image = models.ImageField(upload_to='properties/')
    property_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.property_text
    




    # Create your models here.
