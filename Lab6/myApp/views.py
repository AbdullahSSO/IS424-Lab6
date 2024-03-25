from django.shortcuts import render
from .models import student,course
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.shortcuts import get_object_or_404 

# Create your views here.


class StudnetModelForm(forms.ModelForm):
    class Meta:
     model = student

     fields = ['SID','FirstName','LastName','SPhoneNumber']

class CourseModelForm(forms.ModelForm):
    class Meta:
     model = course
     fields = "__all__"

        

def index(request):
    return render(request,"myApp/index.html",{
        "stu":student.objects.all()
    })


#  this is the details 
def details(request,studentID):

    if request.method == "POST":
        stu = get_object_or_404(student, SID=studentID)
        courseID = request.POST.get("course")
        cours = get_object_or_404(course, CID=courseID)

        stu.coures.add(cours)
        return HttpResponseRedirect(reverse("myApp:details", args=(studentID,)))

    else:
        stu = get_object_or_404(student, SID=studentID)
        myCourses = stu.coures.all()     
        non_courses = course.objects.exclude(CID__in=myCourses).all()

    return render(request,'myApp/details.html',{
        "stu":stu,
        "allcourses": myCourses,
        "nonCourse":non_courses

    })

def createCourse(request):
    if request.method == "POST":
        myForm = CourseModelForm(request.POST)
        
        if myForm.is_valid():
            myForm.save()
            return HttpResponseRedirect(reverse("myApp:createCou"))
    else:
        myForm = CourseModelForm()
        
    return render(request, "myApp/createCourse.html",{
        "form":myForm,
        "allCourses":course.objects.all()
    })



def createStudent(request):
    if request.method == "POST":
        myForm = StudnetModelForm(request.POST)

        if myForm.is_valid: 
           myForm.save()
           return HttpResponseRedirect(reverse("myApp:index"))
        else:
           myForm = StudnetModelForm()
    return render(request, "myApp/createStudent.html", {"form": StudnetModelForm()})

        
