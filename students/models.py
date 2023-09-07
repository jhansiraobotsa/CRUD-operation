from django.db import models

# Create your models here.
class Student(models.Model):
    student_number=models.PositiveIntegerField()
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=40)
    email=models.EmailField(max_length=100)
    field_of_study=models.CharField(max_length=50)
    gpa=models.PositiveIntegerField()

    def __str__(self):
        return f'student: {self.first_name}'