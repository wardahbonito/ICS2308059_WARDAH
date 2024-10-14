from django.shortcuts import render
from library.models import Student, Borrowing, Book, Course, Mentor
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    mystudent = Student.objects.all().values()
    context = {
        'greeting' : 1,
        'mystudent' : mystudent,
    }

    return render (request, "index.html", context)

def view(request):
    context = {
        'firstname': 'aiman',
    }
    return render (request, "view.html", context)

def dbstudent(request):
    mystudent = Student.objects.all().values()
    context = {
        'mystudent': mystudent,
    }
    return render (request, "dbstudent.html", context)

def dbborrow(request):
    myborrow = Borrowing.objects.all().values()
    context = {
        'mystudent': myborrow,
    }
    return render (request, "dbborrow.html", context)

def dbbook(request):
    mybook = Book.objects.all().values()
    context = {
        'mystudent': mybook,
    }
    return render (request, "dbbook.html",context)

def course(request):
    mycourse = Course.objects.all().values()
    dict = {
        'mycourse': mycourse,
    }
    if request.method  == 'POST':
        c_code = request.POST['code']
        c_desc = request.POST['desc']
        data = Course (code = c_code, description=c_desc)
        data.save()
    
    return render (request, "course.html", dict)

def mentor(request):

    mymentor = Mentor.objects.all().values()
    dict = {
        'mymentor': mymentor,
    }

    if request.method  == 'POST':
        c_mentor_id = request.POST['mentor_id']
        c_mentor_name = request.POST['mentor_name']
        c_mentor_room_no = request.POST['mentor_room_no']
        data = Mentor (mentor_id = c_mentor_id, mentor_name = c_mentor_name, mentor_room_no = c_mentor_room_no)
        data.save()

    return render (request, "mentor.html", dict)

def update_course(request,code):
    data = Course.objects.get(code=code)
    dict = {
        'data' : data
    }

    return render (request, "update_course.html", dict)

def save_update_course(request, code):
    c_description = request.POST['desc']
    data = Course.objects.get(code=code)
    data.description = c_description
    data.save()

    return HttpResponseRedirect (reverse("course"))

def update_mentor(request, mentor_id):
    data = Mentor.objects.get(mentor_id=mentor_id)
    dict = {
        'data': data
    }

    return render(request, "update_mentor.html", dict)

def save_update_mentor(request, mentor_id):
    c_mentor_name = request.POST['mentor_name']
    c_mentor_room_no = request.POST['mentor_room_no']
    data = Mentor.objects.get(mentor_id=mentor_id)
    data.mentor_room_no = c_mentor_room_no
    data.mentor_name=c_mentor_name
    data.save()

    return HttpResponseRedirect (reverse("mentor"))

def delete_course(request, code):
    data = Course.objects.get(code=code)
    data.delete()

    return HttpResponseRedirect(reverse('course'))

def delete_mentor(request, mentor_id):
    data = Mentor.objects.get(mentor_id=mentor_id)
    data.delete()

    return HttpResponseRedirect(reverse('mentor'))

def search_course(request):

    if request.method == 'GET':
        c_code = request.GET.get('c_code')

        if c_code:
            data = Course.objects.filter(code=c_code.upper())

        else:
            data = None

        context = {
            'data' : data
        }        
        return render(request, "search_course.html", context)
    
    return render(request, "search_course.html")

def search_mentor(request):

    if request.method == 'GET':
        c_mentor_id = request.GET.get('c_mentor_id')

        if c_mentor_id:
            data = Mentor.objects.filter(mentor_id=c_mentor_id.upper())

        else:
            data = None

        context = {
            'data' : data
        }        
        return render(request, "search_mentor.html", context)
    
    return render(request, "search_mentor.html")
