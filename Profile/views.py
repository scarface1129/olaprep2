from django.shortcuts import render, redirect
from .form1 import RegisterForm
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView
from django.contrib.auth import get_user_model
from .models import Profile, CustomUser
from programs.models import Programs
from django.urls import reverse

User = get_user_model



  
def activate_user_view(request, code=None, *args, **kwargs):
  if code:
      qs = CustomUser.objects.filter(activation_key=code)
      if qs.exists() and qs.count() == 1:
          profile = qs.first()
          if not profile.activated:
             profile.is_active = True 
             profile.save()
             # profile.activated = True
             meeet = profile.id
             program = Programs.objects.get_or_create(id=2)[0]
             profile = Profile.objects.get(id=meeet)
             profile.registered_Course.add(program)

             profile.activation_key = None
             profile.save()
             print("YOU ARE SO VERY WELCOME ")
             return redirect(reverse("login"))
  return redirect(reverse("login"))
# class ActivateView(View):
# 	def get(self,request):
# 		return HttpResponse("you can go ahead and paste your activation code here")


class RegisterView(CreateView):
	form_class = RegisterForm
	template_name = 'registration/register.html'
	success_url = '/'
	# def get_success_url(self):
 #            return "/login"
  


	def dispatch(self,*args,**kwargs):
		# if self.request.user.is_authenticated:
		# 	return redirect('/logout')
		return super(RegisterView,self).dispatch(*args,**kwargs)

