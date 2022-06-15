from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from django.contrib import messages
from .models import CustomUser,Student,Lecturer
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request,"sabiman/index.html")

def user_registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if "@uniben.edu" not in 'email':
            messages.error(request, "This is not uniben account")
            return render(request, "sabiman/user-register.html", {"form": form})
        else:
            if form.is_valid():
                   form.save()
                   #login(request,user,backend='django.contrib.auth.backends.ModelBackend')
                   return redirect('user_login')
    else:
        form = UserRegistrationForm()
    return render(request, "sabiman/user-register.html", {"form": form})

@login_required
def output_user_details(request):
    user_id = request.user.id
    user_details = CustomUser.objects.get(id=user_id)
    if user_id == user_details.id:
        # print("yes")
        context = {
                   "first_name":user_details.first_name,
                   "last_name":user_details.last_name,
                   "department":user_details.department,
                   "faculty":user_details.faculty,
                   "email":user_details.email,

                   }
        return render(request, "sabiman/user-profile.html", {'context':context})

    else:
       messages.error(request,"The user doesn't exist")
       redirect('index')


def student_registration(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            try:
                form.cleaned_data["student_acct_id"] = request.user.id
                student = Student(**form.cleaned_data)
                student.save()
                return HttpResponse("The student is saved in the database")
            except:
                return HttpResponse("The student already exist in the database")
    else:
        form = StudentRegistration()
    return render(request,"sabiman/student_reg.html",{"form":form})


def lecturer_registration(request):
    if request.method == "POST":
        form = LecturerRegistration(request.POST)
        if form.is_valid():
            try:
                form.cleaned_data["lecturer_acct_id"] = request.user.id
                lecturer = Lecturer(**form.cleaned_data)
                lecturer.save()
                messages.success(request,"Your information has successfully been updated")
                return redirect('output_user_details')
            except:
                messages.error(request,"Lecturer already exist in the database,Log in instead.")
                redirect('user_login')
    else:
        form = LecturerRegistration()
    return render(request,"sabiman/lecturer_reg.html",{"form":form})











@login_required
def search_using_mat_no(request):
    if request.method == "POST":
        form = SearchMatNo(request.POST)
        mat_no = request.POST.get('mat_no')
        student_data = Student.objects.filter(mat_no__icontains=mat_no)
        if student_data and student_data.roles != 'class rep':
            return render(request, "sabiman/matno_search.html",
                          {"student_data":student_data})
        else:
            messages.error(request, "The Student does not exist")
            form = SearchMatNo(request.POST)
            return render(request, "sabiman/matno_search.html", {'form': form})
    else:
        form = SearchMatNo()
    return render(request,"sabiman/matno_search.html", {'form':form})

def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,email=email,password=password,backend='django.contrib.auth.backends.ModelBackend')
        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {email}.")
            return redirect("output_user_details")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('user_login')
    else:
        form = UserLoginForm()
    return render(request,'sabiman/user_login.html',{'form':form})


def student_or_lecturer(request):
    #the issue is to make both users not to be clickable at once, but it works
    if request.method == 'POST':
        form = stud_or_lect(request.POST)
        # print(form)
        if form.is_valid():
            user_id = form.cleaned_data.get('user_profile')
            print(user_id)
            if user_id == "STUDENT" :
                return redirect('student_reg')
            elif user_id == "LECT" :
                return redirect('lecturer_reg')
        # else:
        #     messages.error(request,"You can't select two choices")
    else:
        form = stud_or_lect()
    return render (request,'sabiman/stud_lect.html',{"form":form})


def user_logout(request):
    logout(request)
    return redirect('index')