from django.shortcuts import render,redirect
from .models import Student

from django.views import View
# Create your views here.


class home(View):
    def get(self,request):
        stu = Student.objects.all()
        context = {
            'st':stu,
        }
        return render(request,'index.html',context)
        


class addStudent(View):

    def get(self,request):
        return render(request,'addstudent.html')


    def post(self,request):
        
        roll = request.POST.get('roll')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        

        #create an object for models
        s = Student()
        s.roll = roll
        s.name = name
        s.email = email
        s.phone = phone

        s.save()
        return redirect('/')
    
    
class deleteStudent(View):
    
    def get(self,request,roll):
        s = Student.objects.get(pk = roll)
        s.delete()
        return redirect("/")


class updateStudent(View):
    def get(self,request,roll):
        std = Student.objects.get(pk = roll)
        context = {
            'std': std,
        }
        return render(request,"updatestudent.html",context)

    def post(request,roll):

        std = Student.objects.get(pk = roll)
        roll = request.POST.get('roll')
       
        context = {
            'std':std,
        }
        return render(request,"updatestudent.html",context)




