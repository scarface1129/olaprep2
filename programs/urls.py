from django.urls import path
from .views import Tutors, SubjectsListView, RegisterCourse, Registered_Course, Course_OutlineDetailView
from .views import add_to_list_of_courses, AdminsOnly



urlpatterns = [

	path('tutors/', Tutors.as_view(), name = 'tutors'),
	path('subject/', SubjectsListView.as_view(), name = 'subjects'),
	path('registercourse/', RegisterCourse.as_view(), name = 'registercourse'),
	path('add-course/<product_id>', add_to_list_of_courses, name = 'add-course'),
	path('registered-course/', Registered_Course.as_view(), name = 'registered-course'),
	path('course-outline/<slug:slug>/', Course_OutlineDetailView.as_view(), name = 'course-outline'),
	path('admin/', AdminsOnly.as_view(), name = 'admin'),
	# path('bonanza/<pk>', bonanza, name='bonanza'),





]