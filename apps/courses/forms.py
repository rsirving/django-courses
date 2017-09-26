from django.forms import ModelForm
from .models import Course

class courseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'desc']