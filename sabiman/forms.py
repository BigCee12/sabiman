from django import forms
from .models import CustomUser,Student,Lecturer
from .manager import CustomUserManager
from django.contrib.auth.forms import UserCreationForm

Student_level = (
    ("100 Level","100"),
    ("200 Level","200"),
    ("300 Level","300"),
    ("400 Level","400"),
)

PROFILE_CHOICES = (
    ("STUDENT",'STUDENT'),
    ("LECT",'LECTURER'),
)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirmation = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(label="Your UNIBEN Email Address")
    class Meta:
        model= CustomUser
        fields = ['first_name','last_name','email','department',
                  'faculty','account_type',]
        labels = {
            "first_name":"First Name",
            "last_name":"Last Name",
            "faculty":"Faculty",
            "account_type":"Account Type",

        }
        error_messages = {
            "first_name" : {
                "required" : "Please input your first name",
            },
            "last_name" : {
                "required" : "Please input your last name",
            },
            "email": {
                "required" : "Please input your email address"
            },


        }

    def clean_password(self):
        password = self.cleaned_data.get("password")
        password_confirmation = self.cleaned_data.get("password_confirmation")
        if password and password_confirmation:
            if password != password_confirmation:
                raise forms.ValidationError("Passwords don't match")
        return password_confirmation

    def save(self,commit = True):
        user = super(UserRegistrationForm,self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user



class stud_or_lect(forms.Form):
    user_profile = forms.CharField(
        label="Select Profile",widget=forms.RadioSelect(choices=PROFILE_CHOICES))



class StudentRegistration(forms.ModelForm):

    class Meta:
        model = Student
        fields = [
            'mat_no',
            'own_number',
            'own_number_2',
            'student_level',
            'role',
            'relative1_name',
            'relative1_phone',
            'relative2_name',
            'relative2_phone',
            'relative3_name',
            'relative3_phone',

        ]

        labels = {
            'mat_no':'Matriculation Number',
            'own_number':"Your Phone Number",
            'role':'Role',
            'own_number_2': "Phone Number 2",
            'student_level': "Student Level",
            'relative1_name' : "First Relative's Name",
            'relative1_phone': "First Relative's Phone No",
            'relative2_name' : "Second Relative's Name",
            'relative2_phone' : "Second Relative's Phone No",
            'relative3_name' : "Third Relative's Name",
            'relative3_phone' : "Third Relative's Phone",

        }


class LecturerRegistration(forms.ModelForm):
    #level_you_teach = forms.MultipleChoiceField(widget=forms.SelectMultiple,choices=Student_level)
    class Meta:
        model = Lecturer
        fields = ['phone_number_1','phone_number_2','level_you_teach']
        labels  = {
            'level_you_teach' : 'Level(s) you Teach',
            'phone_number_1': 'Primary Phone Number',
            'phone_number_2': 'Phone Number 2',
        }


class SearchMatNo(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['mat_no']
        labels = {
            "mat_no" : "Your Matriculation Number"
        }

class UserLoginForm(forms.ModelForm):
    password = forms.CharField(label="Password",widget=forms.PasswordInput())
    class Meta:
        model = CustomUser
        fields = ['email',]
        labels = {
            "email" : "Email",
        }

