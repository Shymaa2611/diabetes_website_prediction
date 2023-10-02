from django import forms
from .models import DiabetespredictionModel

class checkdiabetesForm(forms.ModelForm):
    class Meta:
        model=DiabetespredictionModel
        fields=('Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','age')
    


