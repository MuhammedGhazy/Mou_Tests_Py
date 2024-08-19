from django import forms
from o_s.models import Student, Track

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('fname', 'lname', 'age', 'relation')

        widgets = {
            'fname': forms.TextInput(attrs={'class': 'form-control'}),
            'lname': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'relation': forms.Select(attrs={'class': 'form-control'})
            
        }

class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ("track_name",)
