from django import forms
from .models import Tematy, Wpisy

class TopicForm(forms.ModelForm):
    class Meta:
        model = Tematy
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Wpisy
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}