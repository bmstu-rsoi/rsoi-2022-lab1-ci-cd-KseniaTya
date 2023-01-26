from django import forms
from .models import Persons

# class DateInput(forms.DateInput):
#     input_type = 'date'

class CreateUpdatePerson(forms.ModelForm):
    class Meta:
        model = Persons
        # fields = ['last_name', 'name', 'father_name', 'birthday',]
        # widgets = {
        #     'birthday': DateInput()
        # }
        fields = ['name', 'address', 'work', 'age']
