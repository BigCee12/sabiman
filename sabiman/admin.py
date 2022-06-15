from django.contrib import admin
from .models import Student,Lecturer, CustomUser,Department,Faculty
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email','first_name','last_name','department','faculty',)
    list_filter = ("is_a_student","is_a_lecturer")


class LecturerAdmin(admin.ModelAdmin):
    # list_display = ("lecturer_acct","level_you_teach",)
    list_filter = ("level_you_teach","is_active",'is_lecturer')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('mat_no','student_acct','own_number','student_level')
    list_filter = ('student_level',)

admin.site.register(Student,StudentAdmin)
admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Lecturer,LecturerAdmin)
admin.site.register(Department)
admin.site.register(Faculty)
