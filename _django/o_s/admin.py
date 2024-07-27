from django.contrib import admin
from .models import Track, Student

# Register your models here.

class CustomStudent(admin.ModelAdmin):
    fieldsets = (
        ['StudentInformation', {'fields': ['fname', 'lname', 'age']}],
        ['ScholarShipInformation', {'fields': ['relation']}]
    )
    list_display = ('fname', 'lname', 'age', 'relation', 'is_graduated')
    list_filter = ['relation', 'fname']
    search_fields = ['fname', 'relation__track_name']

class InlineStudent(admin.StackedInline):
    model = Student
    extra = 2

class CustomTrack(admin.ModelAdmin):
    inlines = [InlineStudent]

admin.site.register(Track, CustomTrack)
admin.site.register(Student, CustomStudent)