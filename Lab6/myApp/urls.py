from django.urls import path
from . import views

app_name ="myApp"
urlpatterns = [
    path("",views.index ,name="index"),
    path('addStudent',views.createStudent,name="createStu"),
    path("createCourse", views.createCourse,name="createCou"),
    path("<str:studentID>",views.details,name="details"),    
]