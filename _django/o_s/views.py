from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Track, Student
from .forms import StudentForm, TrackForm
# Create your views here.

def home (request):
    return HttpResponse ('<h1> This A Home Page </h1>')

def getStudent (request, st_id):
    sd = Student.objects.get(id = st_id)
    context = {'student' : sd}
    return render (request, 'o_s/student_details.html', context)

def getAll (request):
    all_st = Student.objects.all()
    context = {'students' : all_st}
    return render (request, 'o_s/students.html', context)

def new_student(request):
    if request.method=='POST':
        std_form = StudentForm(request.POST)
        if std_form.is_valid():
            std_form.save()
            return HttpResponseRedirect('/all')
    else:
            std_form=StudentForm()
    context = {'st_form' : std_form }
    return render (request,'o_s/new_student.html', context )