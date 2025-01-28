from django import forms
from .models import GuestbookEntry

class GuestbookForm(forms.ModelForm):
    class Meta:
        model = GuestbookEntry
        fields = ['name', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ваше имя', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Ваше сообщение', 'class': 'form-control'}),
        }
