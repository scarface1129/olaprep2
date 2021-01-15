from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from programs.models import Programs
from django.db.models.signals import pre_save, post_save
from .utils import code_generator
from django.urls import reverse
from django.core.mail import send_mail
import os




class UserManager(BaseUserManager):
	def create_user(self,email,password=None,is_active=True,is_staff=False,is_admin=False):
		if not email:
			raise ValueError('user must have an email')
		if not password:
			raise ValueError('user must have a password')

		user_obj = self.model(
				email=self.normalize_email(email)

			)

		user_obj.set_password(password)
		user_obj.is_active = is_active
		user_obj.staff = is_staff
		user_obj.admin = is_admin
		user_obj.save(using=self._db)
	def create_staffuser(self,email,password=None):
		user = self.create_user(
				email,
				password=password,
				is_staff = True

				)
		return user


	def create_superuser(self,email,password=None):
		user = self.create_user(
				email,
				password=password,
				is_staff = True,
				is_admin = True,
				is_active = True

				)
		return user
class CustomUser(AbstractBaseUser,PermissionsMixin):
	email 				= models.EmailField(unique = True)
	is_active 				= models.BooleanField(default=False)
	admin 				= models.BooleanField(default=False)
	staff 				= models.BooleanField(default=False)
	username 			= models.CharField(max_length = 30)
	activation_key      = models.CharField(max_length=120, blank=True, null=True)
	activated           = models.BooleanField(default=False)




	objects = UserManager()


	USERNAME_FIELD = "email"
	def get_full_name():
		return self.email

	def __unicode__(self):
		return self.email

	def get_first_name():
		return self.email


	def get_short_name():
		return self.email

	def __str__(self):
		return self.email
	@property
	def is_staff(self):
		return self.staff

	@property
	def is_admin(self):
		return self.admin

	# @property
	# def is_active(self):
	# 	return self.active


	def has_perm(self, perm, obj = None):
		return True

	def has_module_perms(self,app_label):
		return True

	def send_activation_email(self):
		print("Activation")
		if self.is_active:
			pass
		else:
			self.activation_key = code_generator()#'somekey'
			self.save()
			#path_=reverse()
			path_ = reverse("activate", kwargs={"code":self.activation_key})
			subject = 'Activate Account'
			from_email = 'agboemmanuel002@gmail.com'
			message = f'Activate your account here: {path_}'
			recipient_list = [self.email]
			html_message = f'<p>Activate your account here: {path_}  </p>'
			print(html_message)
			sent_mail= send_mail(
					subject,
					from_email,
					message,
					recipient_list,
					fail_silently=False,
					html_message=html_message)
			
			# sleepy(10)
			return sent_mail
class Profile(models.Model):
	owner				 = models.ForeignKey(CustomUser,on_delete = models.CASCADE)
	registered_Course    = models.ManyToManyField(Programs,blank=True)
	
	def get_registered_Course(self):
		scar = [item.program.Title for item in self.registered_Course.all()]

		return scar

	def __str__(self):
		return self.owner.email

		



def rl_post_save_receiver(sender, instance,created,  *args, **kwargs):
	if created:
		profile, is_created = Profile.objects.get_or_create(owner=instance)
		

post_save.connect(rl_post_save_receiver, sender = CustomUser)

	