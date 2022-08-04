from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from myapp.models import Student
from myapp.forms import Add

# Create your views here.

def index(request):
    want=request.GET.get('q',None)
    if not want:
        details=Student.objects.all()
    else:
        details=Student.objects.filter(name__contains=want)
    return render(request,'myapp/index.html',{'details':details})

def get_student(request,slug=None):
    st=get_object_or_404(Student,slug=slug)
    return render(request,'myapp/stu.html',{'st':st})

def create(request):
    if request.method=='POST':
        form=Add(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            form=Add()
    else:
        form=Add()
    return render(request,'myapp/new.html',{'form':form})

def edit(request,pk=None):
    stu=get_object_or_404(Student,pk=pk)
    if(request.method=='POST'):
        form=Add(request.POST,instance=stu)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form=Add()
    return render(request,'myapp/edit.html',{'form':form})

def delete(request,pk=None):
    stu=get_object_or_404(Student,pk=pk)
    if stu:
        stu.delete()
    return HttpResponse("Deleted "+stu.name+" Succesfully")