from django import forms

from app1.models import employee

class emp_form(forms.ModelForm):
    class Meta:
        model=employee
        fields='__all__'