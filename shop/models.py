from django.conf import settings
from django.db import models
from django.utils import timezone

class Contact(models.Model):
	user_id = models.AutoField(primary_key=True)
	user_name=models.CharField(max_length=50, blank=True, null=True)
	user_email=models.EmailField(max_length=50, blank=True, null=True)
	user_phone=models.CharField(max_length=20, blank=True, null=True)
	user_desc=models.CharField(max_length=200, blank=True, null=True)

	def __str__(self):
		return self.user_name



class Product(models.Model):
    product_name = models.CharField(max_length=50, blank=True, null=True)
    product_price = models.CharField(max_length=10, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    product_pic= models.ImageField(upload_to='post_image', blank=True, null=True)

    def __str__(self):
        return self.product_name


	
