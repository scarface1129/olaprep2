from django.contrib import admin
from .models import Lecture, Registered_Course,Question,Contact


admin.site.register(Lecture)
admin.site.register(Registered_Course)
admin.site.register(Question)
admin.site.register(Contact)

