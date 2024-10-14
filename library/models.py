from django.db import models

# Create your models here.
class Book(models.Model):
    book_id = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    published_year = models.CharField(max_length=4)

class Student(models.Model):
    student_id = models.CharField(max_length=10, primary_key=True)
    student_name = models.CharField(max_length=30)
    student_phone = models.CharField(max_length=10)
    student_email = models.EmailField(max_length=50)
    stud_status = models.CharField(max_length=5, default="active")

class Borrowing(models.Model):
    borrow_id = models.CharField(max_length=10)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    borrow_date = models.DateField(max_length=10)
    return_date = models.DateField(max_length=10)

class Course(models.Model):
    code = models.CharField(max_length=4, primary_key=True)
    description = models.CharField(max_length=5)

class Mentor(models.Model):
    mentor_id = models.CharField(max_length=8, primary_key=True)
    mentor_name = models.CharField(max_length=225)
    mentor_room_no = models.CharField(max_length=3, default='sk2')