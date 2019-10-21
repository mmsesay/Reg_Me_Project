from django.contrib import admin
from fbc_app.models import University, Course, Module, Lecturer, Student

# register the models
admin.site.register(University)
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Lecturer)
admin.site.register(Student)
