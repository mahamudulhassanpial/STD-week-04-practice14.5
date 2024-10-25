from django import forms
from django.core import validators
from django.forms.widgets import NumberInput
from django import forms
import datetime
    


# widgets == field to html input
class contactFrom(forms.Form):
    name = forms.CharField(label = "Full Name : ", help_text="Total lenght must be within 70 charecters", widget = forms.Textarea(attrs = {'id' : 'text_area', 'class' : 'class1 class2', 'placeholder' : 'Enter your name'}))
    name2 = forms.CharField(label = "Full Name : ", initial="Rahim", help_text="Total lenght must be within 70 charecters", required=False)
    # file = forms.FileField()
    # file2 = forms.ImageField()
    email = forms.EmailField(label = "User Email")
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    age = forms.CharField(widget=forms.NumberInput)
    check = forms.BooleanField()
    birthday = forms.CharField(widget=forms.DateInput(attrs= {'type' : 'date'}))
    # birthday = forms.DateField(widget=forms.DateInput(attrs= {'type' : 'date'}))
    appoinment = forms.CharField(widget=forms.DateTimeInput(attrs= {'type' : 'datetime-local'}))
    # appoinment = forms.DateTimeField(widget=forms.DateTimeInput(attrs= {'type' : 'datetime-local'}))
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    # size = forms.CharField(choices = CHOICES, widget= forms.RadioSelect)
    size = forms.ChoiceField(choices = CHOICES, widget= forms.RadioSelect)
    MEAL = [('P', 'Pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices = MEAL,  widget=forms.CheckboxSelectMultiple)
    # pizza = forms.CharField(choices = MEAL, widget=forms.CheckboxSelectMultiple)


def len_check(valu):
    if len(valu) < 10:
        raise forms.ValidationError("Enter a name with at least 10 charas")
class StudentData(forms.Form):
    # name = forms.CharField(validators=[validators.MaxLengthValidator(10, message='Enter a name with at least 10 characters')])
    name = forms.CharField(validators=[validators.MinLengthValidator(10, message='Enter a name with at maximum 10 characters')])
    text = forms.CharField(widget=forms.TextInput, validators=[len_check])
    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message='Enter a valid Email')])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(34, message="age must be at leat 34"), validators.MinValueValidator(24, message="age must be at least 24")])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'], message='File Extend=sion must be ended with .pdf')])

class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.TextInput)
    confirm_password = forms.CharField(widget=forms.TextInput)

    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['name']
        if val_conpass != val_pass:
            raise forms.ValidationError("Password doesn't match")
        if len(val_name) < 15:
            raise forms.ValidationError("Name must be at least 15 charecters")
        
BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']

FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class GeeksForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField() 
    
    first_name = forms.CharField(initial='Your name',max_length = 200) 
    last_name = forms.CharField(max_length = 200) 
    roll_number = forms.IntegerField( 
                     help_text = "Enter 6 digit roll number"
                     ) 
    password = forms.CharField(widget = forms.PasswordInput()) 
    name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField()
    agree = forms.BooleanField(initial=True)
    date = forms.DateField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    email_address = forms.EmailField(required = False,)
    email_address = forms.EmailField( 
    label="Please enter your email address",
)
    message = forms.CharField(
	max_length = 10,
)
    day = forms.DateField(initial=datetime.date.today)
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)
    


