from django.db import models

# Create your models here.
class StudentForm(models.Model):
    first_name  = models.CharField(max_length = 50)
    last_name   = models.CharField(max_length = 50, blank=True, null=True)
    email       = models.EmailField(max_length = 100)
    phone       = models.CharField(max_length = 15)
    address     = models.TextField(blank=True, null=True)
    city        = models.CharField(max_length = 50, blank=True, null=True)
    state       = models.CharField(max_length = 50, blank=True, null=True)
    country     = models.CharField(max_length = 50)
    zip_code    = models.CharField(max_length = 10, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to = 'images/',blank=True, null=True)  
    def __str__(self):
        return self.first_name + ' ' + self.last_name