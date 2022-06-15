from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import ( AbstractBaseUser, PermissionsMixin)
from .manager import CustomUserManager
from django.conf import  settings


Student_level = (
    ("100 Level","100"),
    ("200 Level","200"),
    ("300 Level","300"),
    ("400 Level","400"),
)

account_type = (
    ("Student", "Student"),
    ("Lecturer", "Lecturer")
)

class Faculty(models.Model):
    name = models.CharField(max_length=200,unique=True)
    faculty_code = models.CharField(max_length=5, unique=True)
    email_code = models.CharField(max_length=250,unique=True)
    date_created = models.DateTimeField(auto_created=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = 'Faculties'



class Department(models.Model):
    name =  models.CharField(max_length=200,unique=True)
    faculty = models.ForeignKey(Faculty,related_name='department_faculty',
                                on_delete=models.CASCADE,null=True)
    department_code = models.CharField(max_length=10,unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

lecturer_roles = (
    ("course adviser", "course adviser"),
    ("HOD", "HOD"),
)

student_roles = (
    ("normal", "normal"),
    ("class rep", "class rep"),
)



class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=300, unique=True, )
    first_name = models.CharField(max_length=100,)
    last_name = models.CharField(max_length=100,)
    account_type = models.CharField(choices=account_type, max_length=9,null=True )
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE,
                                null=True)
    department = models.ForeignKey(Department, related_name="user_department",
                                   on_delete=models.CASCADE,null=True)
    is_a_student = models.BooleanField(default=False)
    is_a_lecturer = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Student(models.Model):
    student_acct = models.OneToOneField(CustomUser,on_delete=models.CASCADE,)
    first_name = models.CharField(max_length=100,)
    last_name = models.CharField(max_length=100, )
    mat_no = models.CharField(max_length=10,unique=True,primary_key=True,
                              )
    own_number =  models.CharField(max_length=11, unique=True)
    own_number_2 = models.CharField(max_length=11, unique=True)
    student_level = models.CharField(max_length=50,choices=Student_level,default=100)
    role = models.CharField(max_length=16, choices=student_roles, default="normal",null=True)

    relative1_name = models.CharField(max_length=255,)
    relative1_phone = models.CharField(max_length=11, unique=True,)

    relative2_name = models.CharField(max_length=255,)
    relative2_phone = models.CharField(max_length=11, unique=True,)

    relative3_name = models.CharField(max_length=255,)
    relative3_phone = models.CharField(max_length=11, unique=True,)
    is_student = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)


    def __str__(self):
        return self.mat_no


class Lecturer(models.Model):
    lecturer_acct = models.OneToOneField(CustomUser,on_delete=models.CASCADE,)
    level_you_teach = MultiSelectField(choices=Student_level,default=100)
    phone_number_1 = models.CharField(max_length=11,unique=True,null=True)
    phone_number_2 = models.CharField(max_length=11,unique=True,null=True)
    role = models.CharField(max_length=16, choices=lecturer_roles, default="normal",null=True)
    is_lecturer = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)


    def __str__(self):
        return self.lecturer_acct.first_name







