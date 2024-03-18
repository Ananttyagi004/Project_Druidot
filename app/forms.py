from django import forms
from .models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'address', 'mobile_number', 'email', 'image']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),  # Adjust the number of rows as needed
        }
        