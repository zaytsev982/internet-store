from django.shortcuts import render
from django.http import HttpResponse
from .forms import Userform
from .models import Employee
# Create your views here.


def index2(request):
    if request.method == "POST":
        userform = Userform(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data["name"]
            age = userform.cleaned_data["age"]
            return HttpResponse("<h2>Пользователь - {0}, возраст - {1}</h2>".format(name, age))
        else:
            return HttpResponse("Invalid data")
    else:
        userform = Userform()
        position = "middle developer"
        program_languages = ("Python", "C++", "C#", "Ruby", "Java", "JavaScript", "1C", "Golang")
        personal_data = {"name": "Иван", "second_name": "Иванов", "age": "25 лет"}
        data = {"position": position, "languages": program_languages, "personal_data": personal_data, "form": userform}
        return render(request, "index2.html", context=data)


def users(request, id, name):
    return HttpResponse("<h2>Пользователь - {0}, id - {1}</h2>".format(name, id))


def create(request):
    employee = Employee(name="Максим", age=20)
    employee.save()
    return HttpResponse("Успешно - {0}".format(employee.name))


def index(request):
    return render(request, "index.html")


def add_employee(request):
    return render(request, "add-new-employee.html")