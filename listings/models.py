from django.db import models
from accounts.models import MyUser
from django.core.validators import RegexValidator
import os
from datetime import datetime
from django.utils import timezone


def get_upload_path(instance, filename):
	# if not os.path.exists(f'{instance.seller_user}/{instance.username}/{filename}'):
	# 	os.makedirs(f'{instance.seller_user}/{instance.username}/{filename}')
	return f'{instance.seller_user}/{instance.username}/{filename}'
class Listing(models.Model):
	seller_user = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True)
	freefire_id = models.CharField(max_length=100,unique=True)
	level = models.PositiveIntegerField(validators=[])
	username = models.CharField(unique=True, max_length=264)
	description = models.TextField()
	estimated_price = models.PositiveIntegerField()
	price = models.PositiveIntegerField(blank=True, null=True)

	is_published = models.BooleanField(default=False)
	is_sold = models.BooleanField(default=False)
	signed_up_with = models.CharField(max_length=264, choices=[('Facebook','Facebook'), ('Gmail','Gmail'), ('VK','VK')])
	account_email = models.CharField(unique=True,max_length=264,)
	account_password = models.CharField(max_length=264,)


	photo_main = models.ImageField(upload_to=get_upload_path,)
	video_main = models.FileField(upload_to=get_upload_path)
	posted_date = models.DateTimeField(default=datetime.now)
	def __str__(self):
		return f"{self.freefire_id} ({self.estimated_price})"

		

class Sale(models.Model):
	transaction_id = models.CharField(max_length=55,unique=True)
	ListingAcc = models.ForeignKey(Listing, on_delete=models.SET_NULL, null=True, unique=True)
	customer_user = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True)
	purchased_date = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return f'{self.ListingAcc} ({self.customer_user})'

class PaymentsStore(models.Model):
	customer_user = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True, unique=True)
	ListingAcc = models.ForeignKey(Listing, on_delete=models.SET_NULL, null=True, unique=True)
	phone_num = models.BigIntegerField()
	order_id = models.CharField(max_length=100,unique=True)
	price = models.IntegerField()
class TempStorage(models.Model):
	transaction_id = models.CharField(max_length=55,unique=True)
	buyer = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True)
		