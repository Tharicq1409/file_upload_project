from django import forms
from .models import candidates
from datetime import datetime

class candidate_form(forms.ModelForm):
    year_of_passing = forms.TypedChoiceField(
        coerce=int,
        choices=[(year, year) for year in range(datetime.now().year, 2017, -1)],
        empty_value="Select Year",
        initial=datetime.now().year,
    )
    class Meta:
        model = candidates
        #fields = '__all__'
        fields = {'first_name','last_name','mobile_number','email','street_address','city','state','zip_code','employement_status','year_of_passing','skills','resume'}

        widgets = {
            'first_name' : forms.TextInput(attrs={'style': 'width: 300px;'}),
            'last_name' : forms.TextInput(attrs={'style': 'width: 300px;'}),
            'mobile_number' : forms.TextInput(attrs={'style': 'width: 300px;'}),
            'email' : forms.TextInput(attrs={'style': 'width: 300px;height: 35px'}),
            'street_address' : forms.TextInput(attrs={'style': 'width: 300px;height: 50px'}),
            'city' : forms.TextInput(attrs={'style': 'width: 300px;'}),
            'state' : forms.TextInput(attrs={'style': 'width: 300px;'}),
            'zip_code': forms.TextInput(attrs={'style': 'width: 300px;'}),
            'employement_status': forms.Select(attrs={'style': 'width: 300px; height:40px'}),
            'year_of_passing': forms.NumberInput(attrs={'style': 'width: 300px !important; height: 40px !important;'}),
            'skills' : forms.Textarea(attrs={'style' : 'width:300px;height:50px;border: 1px;border-radius: 4px;background-color: rgba(255, 255, 255, 0.5);'}),
            'resume': forms.FileInput(attrs={'class': 'custom-file-input'}),
        }