from django.urls import path
from .views import *

urlpatterns = [
    path("",index,name='index'),
    path("user_reg/",user_registration,name="user_reg"),
    path('output_user_details/',output_user_details,
         name='output_user_details'),
    path('student_reg/',student_registration,name="student_reg"),
    path('lecturer_reg/',lecturer_registration,name = "lecturer_reg"),
    path('student_search/',search_using_mat_no,name = "search_using_mat_no"),
    path('user_login/',user_login,name='user_login'),
    path('user_logout/', user_logout, name='user_logout'),
    path('select_profile/',student_or_lecturer,name='student_or_lecturer'),
]