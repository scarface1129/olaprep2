from django.db import models
from django.db.models.signals import pre_save, post_save
from django.urls import reverse

from django.db.models import Count


class Program(models.Model):
	Title = models.CharField(max_length=30)


	def __str__(self):
		return self.Title


class Class(models.Model):
	course     = models.CharField(max_length=30)
	program    = models.ForeignKey(Program, on_delete=models.CASCADE)


	def __str__(self):
		return self.course



class Instructors(models.Model):
	name             = models.CharField(max_length=30)
	photo 			 = models.ImageField(upload_to="gallery", null = True)
	sex              = models.CharField(max_length=20)
	qualification    = models.CharField(max_length=1000, default = 'B.Sc')
	phone_no         = models.IntegerField(default= 7085427519)
	slug             = models.SlugField(default='slug')

	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('instructors')

class Programs(models.Model):
	program        = models.OneToOneField(Program, on_delete=models.SET_NULL,null = True)
	course_outline = models.ManyToManyField(Class)
	author         = models.ForeignKey(Instructors, on_delete=models.SET_NULL,null=True)
	price          = models.IntegerField()
	text           = models.TextField(blank = True, null=True)
	slug		   = models.CharField(max_length= 60, null = True, blank =True)

	def __str__(self):
		return self.program.Title

	def get_course_outline(self):
		return self.course_outline
	def get_course_total(self):
		return [ss.course for ss in self.course_outline.all()]
	def get_url(self):
		return reverse('add-course', kwargs={'product_id':self.id})

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
	print("saving...")
	instance.slug = instance.program.Title
pre_save.connect(rl_pre_save_receiver, sender = Programs)





