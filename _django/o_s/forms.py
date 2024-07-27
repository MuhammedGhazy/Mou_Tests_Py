from django import forms
from o_s.models import Student, Track

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('fname', 'lname', 'age', 'relation')

class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ("track_name",)
