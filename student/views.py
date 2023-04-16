from django.shortcuts import render
from student.models import *
from django.views import View

# Create your views here.

class ShowAllStudents(View):
    def get(self,request):

        all_students = Student.objects.filter(flag=True)
        context = {"students":all_students}
        print(context)

        return render(request,"index.html",context)