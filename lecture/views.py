from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View,CreateView,UpdateView,DetailView,ListView
from .forms import QuestionForm, ClassForm, ProgramsForm, ProgramForm, InsrtuctorsForm, ProgramsUpdateForm
from programs.models import Class, Programs, Instructors, Program
from lecture.models import Registered_Course, Lecture, Question
from django.db.models import Q
from Profile.models import CustomUser,Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import ContactForm, LectureForm, LectureForm2, QuestionForm2, ClassForm2
from django.core.mail import send_mail
import pandas as pd
import matplotlib.pyplot as plt

@login_required(login_url = '/login')
def profile(request):
	if request.user.id==1:
		scar = CustomUser.objects.all()
		dan = Profile.objects.all()
		registered_course = Registered_Course.objects.all()
		print(registered_course)
		programs = Programs.objects.all()
		scarface = Class.objects.all()
		scarfac = Class.objects.count()
		print(scarfac)
		students = Profile.objects.count()
		tutors = Instructors.objects.count()
		context={
		'aa':tutors,
		'ee': students,
		'oo': scarfac,
		'programs': programs,
		'class': scarface,
		'object':dan, 'scar':registered_course
		}
		return render(request, 'lecture/profiles.html', context)
	else:
		return redirect(reverse('home'))



class Nothing(View):
	pass
	# return None
class QuestionCreateView(LoginRequiredMixin, CreateView):
	form_class = QuestionForm
	template_name = 'lecture/question.html'
	login_url = '/login/'




	def get_context_data(self, *args, **kwargs):
		context = super(QuestionCreateView, self).get_context_data(*args, **kwargs)
		slug = self.kwargs['slug']
		scar = Question.objects.filter(subject = slug)
		tg = [oo.subject for oo in scar]
		query = self.request.GET.get('q')
		programs = Programs.objects.all()
		programsee = pd.DataFrame(Programs.objects.all().values())
		pltt = programsee.plot(x='id', y='price')
		programse = pd.DataFrame(Program.objects.all().values())
		print(programsee)
		print('------------------------------------------------------------------------')
		programsee['scar'] = programsee['id']
		dd = pd.merge(programsee,programse, on='id').drop(['price','scar'], axis=1)
		if query:
			query.strip()
			scar = Question.objects.filter(
						Q(question__icontains = query)|
						Q(answer__icontains = query)|
						Q(subject__icontains = query)|
						Q(name__icontains = query)

				)
		# context = {'slug': slug, 'programs': programs}
		context['object'] = scar
		context['programs'] = programs
		context['programsee']= programsee.to_html()
		context['programse']= programse.to_html()
		context['dd']= dd.to_html()
		context['pltt']= pltt
		return context


	def form_valid(self,form):
		instance = form.save(commit=False)
		scar = self.kwargs['slug']
		userr = self.request.user
		instance.subject = scar
		print (userr)
		return super(QuestionCreateView, self).form_valid(form)
class QuestionUpdate(LoginRequiredMixin, UpdateView):
	form_class = QuestionForm2
	template_name = 'lecture/questionupdate.html'
	login_url = '/login/'

	def form_valid(self,form):
		instance = form.save(commit=False)
		return super(QuestionUpdate, self).form_valid(form)


	def get_queryset(self):
		slug = self.kwargs['pk']
		return Question.objects.filter(id = slug)
class QuestionListView(ListView):
	model = Question
	template_name = 'lecture/questionlist.html'
class ContactCreateView(CreateView):
	form_class = ContactForm
	template_name = 'lecture/contact.html'
	success_url = '/'
	def get_context_data(self):
		context = super(ContactCreateView, self).get_context_data()
		scar = Programs.objects.all()
		scarfac = Class.objects.count()
		students = Profile.objects.count()
		tutors = Instructors.objects.count()
		# context={
		# 	'aa':tutors,
		# 	'ee': students,
		# 	'oo': scarfac,
		# 	'programs': scar,
		# }
		context['ee'] = students
		context['aa'] = tutors
		context['oo'] = scarfac
		context['programs'] = scar
		return context
	def form_valid(self, form):
		instance = form.save(commit=False)
		subject = 'Message From Client'
		message = instance.comment
		EmailFrom = ['agboemmanuel002@gmail.com']
		EmailTo = instance.email
		sent_mail = send_mail(subject,message,EmailTo,EmailFrom, fail_silently = True)
		return super(ContactCreateView, self).form_valid(form)

		
def contact_us(request):
  context = {}
  return render(request,'contacts.html', context)
def about_us(request):
	scarfac = Class.objects.count()
	print(scarfac)
	students = Profile.objects.count()
	tutors = Instructors.objects.count()
	fan = Programs.objects.all()
	context={
		'aa':tutors,
		'ee': students,
		'oo': scarfac,
		'programs': fan
		
	}
	return render(request,'about_us.html', context)
class LectureDetailView(LoginRequiredMixin, DetailView):
	template_name = 'lecture/lecture.html'

	def get_queryset(self):
		return Lecture.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(LectureDetailView,self).get_context_data(*args,**kwargs)
		slug = self.kwargs['slug']
		print(slug)
		scar = Lecture.objects.filter(slug=slug)
		programs = Programs.objects.all()
		context['programs'] = programs
		context['object'] = scar
		return context

# class FooterView(ListView):
# 	model = Programs
# 	template_name = 'snippets/footer.html'
# 	def get_context_data(self):
# 		context = super(FooterView, self).get_context_data()
# 		programs = Programs.objects.all()
# 		context['programs'] = programs
# 		return context
class LectureCreateView(LoginRequiredMixin,CreateView):
	form_class = LectureForm
	template_name = 'lecture/lecturecreate.html'

	def form_valid(self, form):
		if self.request.user.id==1:
			instance = form.save(commit = False)
			return super(LectureCreateView, self).form_valid(form)
		else:
			return redirect(reverse('home'))
	def get_context_data(self):
		context = super(LectureCreateView, self).get_context_data()
		programs = Programs.objects.all()
		context['programs'] = programs
		return context

class LectureUpdateView(LoginRequiredMixin,UpdateView):
	form_class = LectureForm2
	template_name = 'lecture/lectureupdate.html'

	def form_valid(self, form):
		if self.request.user.id==1:
			instance = form.save(commit = False)
			return super(LectureUpdateView, self).form_valid(form)
		else:
			return redirect(reverse('home'))

	def get_queryset(self):
		slug = self.kwargs['slug']
		return Lecture.objects.filter(slug=slug)
	def get_context_data(self):
		context = super(LectureUpdateView, self).get_context_data()
		programs = Programs.objects.all()
		context['programs'] = programs
		return context
class ClassCreateView(CreateView):
	form_class = ClassForm
	template_name = 'lecture/class.html'
	success_url = '/'

	def form_valid(self,form):
		if self.request.user.id==1:
			instance = form.save(commit=False)
			return super(ClassCreateView,self).form_valid(form)
		else:
			return redirect(reverse('home'))
	def get_context_data(self):
		context = super(ClassCreateView, self).get_context_data()
		programs = Programs.objects.all()
		context['programs'] = programs
		return context

class ClassUpdateView(UpdateView):
	form_class = ClassForm2
	template_name = 'lecture/classupdate.html'
	success_url = '/'

	def form_valid(self,form):
		if self.request.user.id==1:
			instance = form.save(commit=False)
			return super(ClassUpdateView,self).form_valid(form)
		else:
			return redirect(reverse('courses'))
	def get_context_data(self):
		context = super(ClassUpdateView, self).get_context_data()
		programs = Programs.objects.all()
		context['programs'] = programs
		return context
	def get_queryset(self):
		slug = self.kwargs['pk']
		return Class.objects.filter(id = slug)

class CourseListView(ListView):
	model = Class
	template_name = 'lecture/courselist.html'

	def get_context_data(self, *args, **kwargs):
		context = super(CourseListView, self).get_context_data(*args, **kwargs)
		programs = Programs.objects.all()
		courses = Class.objects.all()
		context['object_list'] = courses
		context['programs'] = programs
		return context
class ProgramCreateView(LoginRequiredMixin,CreateView):
	form_class = ProgramForm
	template_name = 'lecture/programcreate.html'
	success_url = '/'

	def form_valid(self, form):
		if self.request.user.id==1:
			instance = form.save(commit = False)
			return super(ProgramCreateView, self).form_valid(form)
		else:
			return redirect(reverse('home'))
	def get_context_data(self):
		context = super(ProgramCreateView, self).get_context_data()
		programs = Programs.objects.all()
		context['programs'] = programs
		return context
class ProgramsCreateView(LoginRequiredMixin,CreateView):
	form_class = ProgramsForm
	template_name = 'lecture/programscreate.html'
	success_url = '/'

	def form_valid(self, form):
		if self.request.user.id==1:
			instance = form.save(commit = False)
			return super(ProgramsCreateView, self).form_valid(form)
		else:
			return redirect(reverse('home'))
	def get_context_data(self, *args, **kwargs):
		context = super(ProgramsCreateView, self).get_context_data(*args, **kwargs)
		programs = Programs.objects.all()
		context['programs'] = programs
		return context
class ProgramsUpdateView(LoginRequiredMixin,UpdateView):
	form_class = ProgramsUpdateForm
	template_name = 'lecture/programupdate.html'
	success_url = '/'

	def form_valid(self, form):
		if self.request.user.id==1:
			instance = form.save(commit = False)
			return super(ProgramsUpdateView, self).form_valid(form)
		else:
			return redirect(reverse('programs'))
	def get_context_data(self, *args, **kwargs):
		context = super(ProgramsUpdateView,self).get_context_data(*args,**kwargs)
		programs = Programs.objects.all()
		context['programs'] = programs
		return context

	def get_queryset(self, *args, **kwargs):
		slug = self.kwargs['slug']
		# print(slug)

		return Programs.objects.filter(slug = slug)
	def get_form_kwargs(self):
		kwargs = super(ProgramsUpdateView, self).get_form_kwargs()
		slug = self.kwargs['slug']
		# print(slug)
		kwargs['slug'] = slug
		return kwargs
class ProgramListView(ListView):
	model = Programs
	template_name = 'programs/programlist.html'

	def get_context_data(self, *args, **kwargs):
		context = super(ProgramListView,self).get_context_data(*args,**kwargs)
		programs = Programs.objects.all()
		context['object_list'] = programs
		context['programs'] = programs
		return context

class ProgramsListView(ListView):
	model = Program
	template_name = 'lecture/programlist.html'

def get_context_data(self, *args, **kwargs):
	context = super(ProgramsListView,self).get_context_data(*args,**kwargs)
	scar = Program.objects.all()
	programs = Programs.objects.all()
	context['object_list'] = scar
	context['programs'] = programs
	return context
def tutors_deleteview(request, item_id):
	print(item_id)
	item_to_del = Instructors.objects.filter(pk = item_id)
	print(item_to_del)
	if item_to_del.exists():
		item_to_del[0].delete()
		return redirect(reverse('instructors'))
def class_deleteview(request, item_id):
	print(item_id)
	item_to_del = Class.objects.filter(pk = item_id)
	print(item_to_del)
	if item_to_del.exists():
		item_to_del[0].delete()
		return redirect(reverse('courses'))
def program_deleteview(request, item_id):
	print(item_id)
	item_to_del = Program.objects.filter(pk = item_id)
	print(item_to_del)
	if item_to_del.exists():
		item_to_del[0].delete()
		return redirect(reverse('program'))
def deleteview(request, item_id):
	print(item_id)
	item_to_del = Programs.objects.filter(pk = item_id)
	print(item_to_del)
	if item_to_del.exists():
		item_to_del[0].delete()
		return redirect(reverse('programs'))
def deleteviews(request, item_id):
	print(item_id)
	item_to_del = Lecture.objects.filter(pk = item_id)
	print(item_to_del)
	if item_to_del.exists():
		item_to_del[0].delete()
		return redirect(reverse('lectures'))

class LectureListView(ListView):
	model = Lecture
	template_name = 'lecture/lecturelist.html'

	def get_context_data(self, *args, **kwargs):
		context = super(LectureListView, self).get_context_data(*args, **kwargs)
		programs = Programs.objects.all()
		lecture = Lecture.objects.all()
		context['object_list'] = lecture
		context['programs'] = programs
		return context
class InstructorsCreateView(LoginRequiredMixin,CreateView):
	form_class = InsrtuctorsForm
	template_name = 'lecture/instructorscreate.html'
	success_url = '/'

	def form_valid(self, form):
		if self.request.user.id==1:
			instance = form.save(commit = False)
			scar = instance.name
			print(scar)
			instance.slug = scar
			return super(InstructorsCreateView, self).form_valid(form)
		else:
			return redirect(reverse('home'))
class InsructorsListView(LoginRequiredMixin,ListView):
	model = Instructors
	template_name = 'lecture/instructors.html'
class InstructorsUpdateView(LoginRequiredMixin,UpdateView):
	form_class = InsrtuctorsForm
	template_name = 'lecture/instructorsupdate.html'

	def form_valid(self, form):
		if self.request.user.id==1:
			instance = form.save(commit = False)
			
			return super(InstructorsUpdateView, self).form_valid(form)
		else:
			return redirect(reverse('home'))
	def get_queryset(self):
		slug = self.kwargs['slug']
		return Instructors.objects.filter(name=slug)
