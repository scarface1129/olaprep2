from .views import RegisterView, activate_user_view
from django.urls import path

urlpatterns = [
    path('register/', RegisterView.as_view(), name ='register'),
    path('<code>/', activate_user_view, name ='activate'),
    
    



    ]