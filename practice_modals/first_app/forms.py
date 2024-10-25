from django import forms
from .models import MyModel

class PostFrom(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = '__all__'