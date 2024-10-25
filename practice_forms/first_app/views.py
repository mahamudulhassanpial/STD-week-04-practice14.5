from django.shortcuts import render
from . forms import contactFrom,GeeksForm


# Create your views here.

def home(request):
    return render(request, './first_app/home.html')

def about(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request, './first_app/about.html', {'name' : name, 'email' : email, 'select' : select})
    else:
        return render(request, './first_app/about.html',)
    

def submit_form(request):
    return render(request, './first_app/form.html')

def DjangoForm(request):
    if request.method == 'POST':
        form = contactFrom(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = contactFrom()
    return render(request, './first_app/django_form.html', {'form':form})


def Geeks_Form(request):
    if request.method == 'POST':
        form = GeeksForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = GeeksForm()
    return render(request, './first_app/django_form.html', {'form':form})


