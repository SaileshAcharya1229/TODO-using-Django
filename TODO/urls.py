from django.urls import path
from . import views

urlpatterns = [
 
    path("",views.home.as_view(),name="home"),
    #path("",views.home),
    path("addstudent", views.addStudent.as_view()),
    path("deletestudent<int:roll>",views.deleteStudent.as_view()),
    path("updatestudent<int:roll>",views.updateStudent.as_view())

]