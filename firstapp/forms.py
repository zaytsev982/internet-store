from django import forms


class Userform(forms.Form):
    name = forms.CharField(label="Имя", min_length=2, max_length=32)
    second_name = forms.CharField(label="Фамилия", min_length=2, max_length=32)
    age = forms.IntegerField(label="Возраст", max_value=100, min_value=5)
    gender = forms.CharField(label="Пол", max_length=10)
