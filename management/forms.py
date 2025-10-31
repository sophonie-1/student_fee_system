from django import forms
from .models import Student, FeeStructure, Payment

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'program', 'campus', 'year_of_study']
        widgets = {
            'student_id': forms.TextInput(attrs={'placeholder': 'e.g., S001'}),
            'year_of_study': forms.NumberInput(attrs={'min': 1}),
        }

class FeeStructureForm(forms.ModelForm):
    class Meta:
        model = FeeStructure
        fields = ['program', 'year', 'total_fee']
        widgets = {
            'year': forms.NumberInput(attrs={'min': 1}),
            'total_fee': forms.NumberInput(attrs={'min': 0}),
        }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['student', 'amount']
        widgets = {
            'amount': forms.NumberInput(attrs={'min': 1}),
        }