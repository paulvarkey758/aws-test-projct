from django.urls import path
from student.views import *

urlpatterns = [
    path('show/',ShowAllStudents.as_view()),
]