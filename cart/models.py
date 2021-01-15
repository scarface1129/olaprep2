from django.db import models
from programs.models import Programs
from Profile.models import Profile
from django.db.models.signals import pre_save, post_save




class Order_item(models.Model):
	product = models.OneToOneField(Programs, on_delete = models.SET_NULL,null=True)
	is_ordered = models.BooleanField(default=False)
	date_ordered = models.DateField(auto_now = True)

	def __str__(self):
		return self.product.program.Title



class Order(models.Model):
	owner = models.ForeignKey(Profile, on_delete = models.SET_NULL, null = True)
	items = models.ManyToManyField(Order_item)
	is_ordered = models.BooleanField(default=False)
	ref_code = models.CharField(max_length=50, null = True, blank =True)
	date_ordered = models.DateField(auto_now = True, null = True,blank=True)


	def __str__(self):
		return self.owner.owner.email

	def get_total_price(self):
		return sum([item.product.price for item in self.items.all()])

class Free(models.Model):
	promo = models.IntegerField(null = True, blank = True)
	is_On = models.BooleanField(default=False)
	christmas = models.BooleanField(default=False)
	new_year = models.BooleanField(default=False)
	thanksgiving = models.BooleanField(default=False)
	easter = models.BooleanField(default=False)		


	