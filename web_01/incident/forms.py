from .models import Incidents
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class IncidentsForm(ModelForm):
    class Meta:
        model = Incidents
        fields = ["tip","contact","full_text_incident","date"]

        widgets = {
        "tip": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Тип инцидента: вирус, спам ...'
        }),
        "contact": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Почта'
        }),

        "full_text_incident": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Детали инцидента'
        }),
        "date": DateTimeInput(attrs={
                'type':'datetime-local',
                'class': 'form-control',
                'placeholder': 'Дата'
            })

        }


