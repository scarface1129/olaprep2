from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth.admin import Group
from .models import Profile

# Register your models here.
class CustomUserAdmin(UserAdmin):
	form     = UserChangeForm
	add_form = UserCreationForm
	model    = CustomUser
	list_display = ['email','is_active','admin','staff']
	list_filter = ('admin','staff','is_active')
	search_fields  = ['email']

    


admin.site.register(Profile)

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.unregister(Group)