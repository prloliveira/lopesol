from django import forms
from .models import UserData

class DataCollectionForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['gender', 'birth_date', 'year_joined', 'unit_area', 'function']
