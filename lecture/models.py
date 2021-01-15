from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from Profile.models import CustomUser

from programs.models import Programs,Class
class Lecture(models.Model):
	documentation = models.TextField(default='documentation')
	text          = models.TextField(default='text')
	lecture       = models.ForeignKey(Class, on_delete=models.CASCADE)
	slug          = models.SlugField(default='slug')
	name          = models.CharField(max_length=500, default = '')
	videofile     = models.FileField(upload_to='videos/', null=True, verbose_name="")
	def __str__(self):
		return self.slug
	def get_absolute_url(self):
		return reverse('lec', kwargs={'slug':self.lecture})

	def get_url(self):
		return reverse('question', kwargs={'slug':self.slug})
		
def rl_pre_save_receiver(sender, instance, *args, **kwargs):
	print("saving...")
	instance.slug = instance.lecture.course
	instance.name = instance.lecture.course
pre_save.connect(rl_pre_save_receiver, sender = Lecture)





class Registered_Course(models.Model):
	owner = models.ForeignKey(CustomUser,on_delete = models.CASCADE)
	course = models.ManyToManyField(Programs)

	def __str__(self):
		return self.owner.email


class Question(models.Model):
	name     = models.CharField(unique = True,max_length=  30)
	question = models.TextField()
	answer   = models.TextField(blank=True,null = True)
	subject  = models.CharField(max_length =30, blank = True, null=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('question', kwargs={'slug':self.subject})
class Contact(models.Model):
	name = models.CharField(max_length = 100, null=False, blank=False)
	email = models.EmailField()
	comment = models.TextField(max_length=1000)
	def __str__(self):
		return self.name