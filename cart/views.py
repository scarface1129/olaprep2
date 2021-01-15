from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from Profile.models import Profile
from programs.models import Program, Programs
from django.contrib import messages
from django.views.generic import View,ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import Order_item,Order
from datetime import date
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from lecture.models import Registered_Course

# from django.views.decorators.csrf import csrf_exempt # new
# import stripe
# from django.conf import settings # new
# from django.http.response import JsonResponse
class Cart(LoginRequiredMixin,ListView):
	model = Order_item
	template_name = 'cart/cart.html'

	def get_context_data(self, *args,**kwargs):
		context = super(Cart, self).get_context_data(*args, **kwargs)
		profile = get_object_or_404(Profile,owner = self.request.user)
		order  = Order.objects.filter(owner =profile ,is_ordered=False).first()
		if order==None:
			scar = None
			programs = Programs.objects.all()
			context['programs'] = programs
			context['object_list'] = scar
			return context

		else:
			scar = order.items.all()
			programs = Programs.objects.all()
			context['programs'] = programs
			context['object_list'] = scar
			return context



class Checkout(LoginRequiredMixin,ListView):
	def get(self, request):
		profile = get_object_or_404(Profile,owner = self.request.user)
		order  = Order.objects.filter(owner =profile ,is_ordered=False).first()
		scar = order.items.all()
		scarface = [item.product.price for item in scar]
		scarface = sum(scarface)
		print(scarface)
		programs = Programs.objects.all()
			
		context = {'object_list':scar,'objects':scarface, 'og':order, 'programs':programs}
		return render(request,'cart/checkout.html', context)
@login_required(login_url = '/login')
def delete(request,item_id):
	item_to_delete = Order_item.objects.filter(pk=item_id)
	if item_to_delete.exists():
		item_to_delete[0].delete()
		messages.info(request,'Course has been deleted')
	return redirect(reverse('cart:cart'))

@login_required(login_url = '/login')
def process_payment(request,order_id):

	return redirect(reverse('cart:update',kwargs={'order_id':order_id}))


@login_required(login_url = '/login')
def payment_complete(request,order_id):
	if request.method=='POST':
		data = json.loads(request.POST.get('payload'))
		if data('status') == 'succeeded':
			pass
			return render(request,'',{})
	else:
		order_to_purchase = Order.objects.filter(pk = order_id).first()
		order_to_purchase.is_ordered = True
		order_to_purchase.date_ordered = datetime.datetime.now()
		order_to_purchase.save()
		order_list = order_to_purchase.items.all()
		order_list.update(is_ordered=True,date_ordered=datetime.datetime.now())
		user_profile = get_object_or_404(Profile,owner=request.user)
		ordered_course = [item.product for item in order_list]
		print(ordered_course)
		print(ordered_course)
		print(ordered_course)
		user_profile.owner = request.user
		user_profile.registered_Course.add(*ordered_course)
		user_profile.save()
		reg_course = Registered_Course.objects.get_or_create(owner = request.user)[0]
		reg_course.course.add(*ordered_course)
		reg_course.save()
		return redirect(reverse('registered-course'))
		# return render(request,'cart/sss.html',{})



