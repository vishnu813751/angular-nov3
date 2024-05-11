from django.shortcuts import render,redirect
# from django.http import HttpResponse
from employee.models import Employee
from employee.forms import EmployeeForm



def index(re):
    return render(re,'index.html')
def base(re):
    return render(re,'base.html')
def emp(request):
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form=EmployeeForm()
    return render(request,'index.html',{'form':form})

def show(request):
    employee=Employee.objects.all()
    return render(request,'show.html',{'employees':employee})

def edit(request,id):
    employee=Employee.objects.get(id=id)
    return render(request,'edit.html',{'employee':employee})

def update(request,id):
    employee=Employee.objects.get(id=id)
    form=EmployeeForm(request.POST,instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request,'edit.html',{'employee':employee})

def delete(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")

def register(request):
    return render(request,'reg.html')


def view_employee(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'view.html', {'employee':employee})




def editup(request, id):
    if request.method == "POST":
        employee = Employee.objects.get(id=id)
        employee.ename = request.POST.get('ename')
        employee.eemail = request.POST.get('eemail')
        employee.econtact = request.POST.get('econtact')
        employee.save()
        return redirect('show')
    # Handle GET request or any other logic
    # ...