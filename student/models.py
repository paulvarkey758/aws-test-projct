from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    age = models.IntegerField()
    roll_no = models.IntegerField()
    total_mark = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    flag = models.BooleanField(default=True)

    def __str__(self):
        return self.name