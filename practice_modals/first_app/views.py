from django.shortcuts import render, redirect
from . import models
from django.utils import timezone
from first_app.models import MyModel
import uuid





def add_student(request):
    # Example of adding a student entry
    student = MyModel.objects.create(
        name="John Doe", 
        roll=MyModel.objects.count() + 1,
        father_name="Father Name",
        address="123 Elm St",
        date_field="2024-01-01",
        date_time_field="2024-01-01 12:00:00",
        decimal_field=3.14,
        duration_field="00:30:00",
        email_field="john@example.com",
        file_field=None,
        float_field=3.14,
        generic_ip_address_field="192.168.1.1",
        integer_field=123,
        json_field={"key": "value"},
        positive_integer_field=10,
        text_field="Sample text",
        time_field="12:00:00",
        uuid_field=uuid.uuid4()
    )
    student.save()
    return redirect("homepage")

def home(request):
    student = models.MyModel.objects.all()
    print(f"Number of students: {student.count()}")
    return render(request, "home.html", {'data' : student})

def delete_student(request, roll):
    std = models.MyModel.objects.get(pk = roll).delete()
    return redirect("homepage")
