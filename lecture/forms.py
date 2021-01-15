from django import forms
from .models import Question
from programs.models import Class,Program, Programs, Instructors
from .models import Contact, Lecture


class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = [
			'name',
			'question',

		]
class QuestionForm2(forms.ModelForm):
	class Meta:
		model = Question
		fields = [
			'name',
			'question',
			'answer',
		]



class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = [

			'name',
			'email',
			'comment',
		]


class LectureForm(forms.ModelForm):
	class Meta:
		model = Lecture
		fields = [

			
			'documentation',
			'text',
			'lecture',
			'slug',
			'name',
			'videofile',


		]
	def __init__(self, *args, **kwargs):
		super(LectureForm, self).__init__(*args, **kwargs)
		self.fields['lecture'].queryset = Class.objects.all().exclude(lecture__isnull=False)


class LectureForm2(forms.ModelForm):
	class Meta:
		model = Lecture
		fields = [

			
			'documentation',
			'text',
			'lecture',
			'slug',
			'name',
			'videofile',


		]


class ClassForm(forms.ModelForm):
	class Meta:
		model = Class
		fields = [

			'course',
			'program',

		]

	def __init__(self,*args, **kwargs):
		super(ClassForm, self).__init__(*args, **kwargs)
		self.fields['program'].queryset=Program.objects.all()

class ClassForm2(forms.ModelForm):
	class Meta:
		model = Class
		fields = [

			'course',
			'program',

		]
class ProgramForm(forms.ModelForm):
	class Meta:
		model = Program
		fields = [

			'Title',
			

		]


class ProgramsForm(forms.ModelForm):
	class Meta:
		model = Programs
		fields = [

			'program',
			'course_outline',
			'author',
			'price',
			'text',
			'slug',

		]
	def __init__(self,*args, **kwargs):
		super(ProgramsForm, self).__init__(*args, **kwargs)
		self.fields['course_outline'].queryset=Class.objects.all().exclude(programs__isnull=False)
class ProgramsUpdateForm(forms.ModelForm):
	class Meta:
		model = Programs
		fields = [

			'program',
			'course_outline',
			'author',
			'price',
			'text',
			'slug',

		]
	def __init__(self,slug, *args, **kwargs):
		print(slug)
		print(slug + 'scarface')

		super(ProgramsUpdateForm, self).__init__(*args, **kwargs)
		self.fields['course_outline'].queryset=Class.objects.all()


class InsrtuctorsForm(forms.ModelForm):
	class Meta:
		model = Instructors
		fields = [

			'name',
			'sex',
			'qualification',
			'phone_no',

		]