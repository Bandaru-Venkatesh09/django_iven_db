from django.shortcuts import render,redirect

from app1.models import employee
from app1.form import emp_form

def details(request):
    data=employee.objects.all()
    context={
        'data':data
    }
    return render(request,'home.html',context)

def add_emp(request):
    form=emp_form()
    if request.method=='POST':
        form=emp_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=emp_form()
    context={
        'form':form
    }
    return render(request,'form.html',context)
            
