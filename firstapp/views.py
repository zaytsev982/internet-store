from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Userform
from .models import Employee
# Create your views here.


def index(request):
    return render(request, "index.html")


def add_employee(request):
    if request.method == "POST":
        userform = Userform(request.POST)
        if userform.is_valid():
            employee = Employee(name=userform.cleaned_data["name"], age=userform.cleaned_data["age"])
            employee.save()
            return HttpResponseRedirect("/index/")
        else:
            return HttpResponse("Invalid data")
    userform = Userform()
    data = {"form": userform}
    return render(request, "add-new-employee.html", context=data)


# def save(request):
#     return render(request, "index.html")
