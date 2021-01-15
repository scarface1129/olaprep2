from django.shortcuts import render, get_object_or_404, redirect
from .models import Programs, Class, Instructors
from django.views.generic import View, ListView,DetailView,UpdateView,DeleteView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from Profile.models import Profile
from django.contrib import messages
from django.urls import reverse
from cart.models import Order_item, Order, Free
from cart.extras import genetrate_order_id
from django.contrib.auth.decorators import login_required
from django.contrib import messages



@login_required(login_url = '/login')
def add_to_list_of_courses(request,**kwargs):
	#get the user 
	user = get_object_or_404(Profile, owner = request.user)
	print (user)
	print (user)
	course = Programs.objects.filter(id = kwargs.get('product_id', '')).first()
	profile = Profile.objects.filter(owner=request.user)
	if course in Profile.objects.get(owner=request.user).registered_Course.all():
		messages.info(request,'You Already Registered For The Course')
		return redirect(reverse('/'))
	order_item, status = Order_item.objects.get_or_create(product = course)
	order = Order.objects.get_or_create(owner = user, is_ordered=False)[0]
	order.items.add(order_item)
	if status:
		order.ref_code = genetrate_order_id()
		order.save
	messages.info(request, 'The Course Has Been Added Successfully')
	return redirect(reverse('registercourse'))

def home(request):
	scar = Programs.objects.all()

	if request.method == 'GET':
		messages.error(request,'e done happen ooooooooo')
	# print(scarfac)	
	scarface = Class.objects.all()
	scarfac = Class.objects.count()
	students = Profile.objects.count()
	tutors = Instructors.objects.count()
	
	
	context={
		'aa':tutors,
		'ee': students,
		'oo': scarfac,
		'programs': scar,
		'class': scarface
	}
	return render(request,'home.html',context)


class Tutors(LoginRequiredMixin, ListView):
	model = Instructors
	template_name = 'programs/tutors.html'

# def bonanza(request, pk):
# 	deduction1 = Free.objects.filter(id=1)
# 	deduction = [oo.promo for oo in deduction1][0]
# 	deduction3 = [oo.is_On for oo in deduction1][0]
# 	print(deduction)
# 	programs = Programs.objects.all()
# 	for price in Programs.objects.all():
# 		dd=Programs.objects.filter(id=pk)
# 		print(dd)

# 		if deduction3 is True and deduction is not None:
# 			new_price = int(price.price-deduction)
# 			dd.update(price = new_price)
# 			print(new_price)
# 		elif deduction3 is False and deduction is not None: 
# 			new_price = int(price.price+deduction)
# 			dd.update(price = new_price)

# 		return redirect(reverse('home'))

class SubjectsListView(LoginRequiredMixin,ListView):
	model = Programs
	template_name = 'programs/subject.html'
	def get_context_data(self, *args, **kwargs):
		context = super(SubjectsListView, self).get_context_data(*args, **kwargs)
		# slug = self.kwargs['slug']
		# user_profile = Programs.objects.all().first()
		# user_profile=Programs.course_outline
		# outline = [item for item in user_profile]
		# print(outline)
		scar = Programs.objects.all()
		context={
			'programs': scar
		}
		context['object_list'] = scar
		return context


def get_user_pending_product(request):
	profile = get_object_or_404(Profile, owner = request.user)
	ordered = Order.objects.filter(owner = profile, is_ordered = False)
	if ordered.exists():
		return ordered[0]
	return 0

class RegisterCourse(LoginRequiredMixin,ListView):
	def get(self, request):
		program = Programs.objects.all()
		registercourse = Profile.objects.get(owner=self.request.user).registered_Course.all()
		profile = get_object_or_404(Profile, owner = self.request.user)
		scarp = Programs.objects.all()
		scarfac = Class.objects.count()
		students = Profile.objects.count()
		tutors = Instructors.objects.count()
		# deduction1 = Free.objects.filter(id=1)
		# promo = [oo.promo for oo in deduction1][0]
		# if promo != None:
		# 	deduction = str(promo)
		# 	print(promo)
		# else:
		# 	promo = None
		# print (deduction + 'is d promo deduction')

		if Order.objects.filter(owner = profile, is_ordered = False).first():

			ordered = Order.objects.filter(owner = profile, is_ordered = False).first()

			scar = ordered.items.all()
			

		# print(scar)
		# ordered = ordered[0]
		# scarface = ordered
		# scarface = get_user_pending_product(request)
			current_ordered = [item.product for item in scar]
		else:	
			current_ordered = None
		context = {'object_list':program,
					'scarp':registercourse,
					'scarface':current_ordered,
					# 'promo':promo,
					'aa':tutors,
					'ee': students,
					'oo': scarfac,
					'programs': scarp



					}
		return render(request, 'programs/registercourse.html', context)


	# def get_form_kwargs(self, *args, **kwargs):
	# 	kwargs= super(RegisterCourse).get_form_kwargs(*args, **kwargs)
	# 	free = Free.objects.all()
	# 	ff = [oo.christmas for oo in free][0]
	# 	print(ff)
	# 	if ff==False:
	# 		scaree = 50
	# 		kwargs['scar'] = scaree
	# 		print(kwargs)
class Registered_Course(LoginRequiredMixin,ListView):
	model = Profile
	template_name = 'programs/registered_course.html'

	def get_context_data(self, *args, **kwargs):
		context = super(Registered_Course, self).get_context_data(*args, **kwargs)
		user_profile = Profile.objects.get(owner = self.request.user).registered_Course.all()
		# registered_course = [item.registered_Course for item in user_profile]
		print(user_profile)
		scar = Programs.objects.all()
		scarfac = Class.objects.count()
		students = Profile.objects.count()
		tutors = Instructors.objects.count()
		context={
			'aa':tutors,
			'ee': students,
			'oo': scarfac,
			'programs': scar,
		}
		context['object'] = user_profile
		return context


class Course_OutlineDetailView(DetailView):
	template_name = 'programs/course_outline.html'
	def get_queryset(self):
		return Programs.objects.all()
	def get_context_data(self, *args, **kwargs):
		context = super(Course_OutlineDetailView, self).get_context_data(*args, **kwargs)
		slug = self.kwargs['slug']
		user_profile = Programs.objects.filter(slug=slug).first()
		user_profile=user_profile.course_outline.all()
		outline = [item for item in user_profile]
		print(outline)
		scar = Programs.objects.all()
		context={
			'programs': scar
		}
		context['object'] = user_profile
		return context

	


class AdminsOnly(View):
	def get(self, request):
		if self.request.user.id==1:
			scar = Programs.objects.all()
			scarface = Class.objects.all()
			scarfac = Class.objects.count()
			print(scarfac)
			students = Profile.objects.count()
			tutors = Instructors.objects.count()
			context={
			'aa':tutors,
			'ee': students,
			'oo': scarfac,
			'programs': scar,
			'class': scarface
			}
			return render(request, 'programs/admin.html', context)
		else:
			return redirect(reverse('home'))