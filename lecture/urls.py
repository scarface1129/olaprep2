# from .views import 
from django.urls import path
from .views import class_deleteview,program_deleteview,ClassUpdateView,tutors_deleteview, QuestionCreateView, InstructorsUpdateView,LectureDetailView,LectureListView, LectureCreateView, ClassCreateView, InstructorsCreateView
from .views import profile,CourseListView,ProgramsListView,deleteview,deleteviews, InsructorsListView, QuestionListView, QuestionUpdate, ContactCreateView, ProgramsCreateView, ProgramCreateView, ProgramsUpdateView,ProgramListView,LectureUpdateView

urlpatterns = [
 
	path('question/<slug>/', QuestionCreateView.as_view(), name = 'question'),
	path('question-update/<pk>/', QuestionUpdate.as_view(), name = 'question-update'),
	path('dets/<slug:slug>/', LectureDetailView.as_view(), name ='lec'),
	path('update-lecture/<slug:slug>/', LectureUpdateView.as_view(), name ='update-lecture'),
	path('profiles/', profile, name = 'profile'),
	path('contact/', ContactCreateView.as_view(), name = 'contact'),
	path('create-lecture/', LectureCreateView.as_view(), name = 'create-lecture'),
	path('create-class/', ClassCreateView.as_view(), name = 'create-class'),
	path('create-programs/', ProgramsCreateView.as_view(), name = 'create-programs'),
	path('create-program/', ProgramCreateView.as_view(), name = 'create-program'),
	path('create-instructors/', InstructorsCreateView.as_view(), name = 'create-instructors'),
	path('update-tutors/<slug>', InstructorsUpdateView.as_view(), name = 'update-tutors'),
	path('update-class/<pk>', ClassUpdateView.as_view(), name = 'update-class'),
	path('update-programs/<slug>/', ProgramsUpdateView.as_view(), name = 'update-programs'),
	path('programs/', ProgramListView.as_view(), name = 'programs'),
	path('courses/', CourseListView.as_view(), name = 'courses'),
	path('lectures/', LectureListView.as_view(), name = 'lectures'),
	path('instructors/', InsructorsListView.as_view(), name = 'instructors'),
    path('question/', QuestionListView.as_view(), name = 'question'),
    path('program/', ProgramsListView.as_view(), name = 'program'),
    path('delete_item/<item_id>/', deleteview, name = 'deletes'),
    path('delete_programs/<item_id>/', deleteviews, name = 'deletese'),
    path('delete_program/<item_id>/', program_deleteview, name = 'delete_program'),
    path('delete_tutor/<item_id>/', tutors_deleteview, name = 'delete_tutor'),
    path('delete_class/<item_id>/', class_deleteview, name = 'delete_class'),
    

    






     ]