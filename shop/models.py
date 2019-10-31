from django.conf import settings
from django.db import models
from django.utils import timezone

class Contact(models.Model):
	user_id = models.AutoField(primary_key=True)
	user_name=models.CharField(max_length=50, blank=False)
	user_email=models.EmailField(max_length=50, blank=False)
	user_phone=models.CharField(max_length=20, blank=False)
	user_desc=models.CharField(max_length=200, blank=False)

	def __str__(self):
		return self.user_name



class Product(models.Model):
    product_name = models.CharField(max_length=256, blank=False)
    product_price = models.IntegerField(blank=False)
    desc = models.TextField(blank=False)
    product_image= models.ImageField(upload_to='post_image', blank=True, null=True)

    def __str__(self):
        return self.product_name


	
