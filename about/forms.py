# Django
from django import forms

# Local Django
from . models import Contact


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'mb-2'})
        self.fields['email'].widget.attrs.update({'class': 'mb-2'})
        self.fields['subject'].widget.attrs.update({'class': 'mb-2'})
        self.fields['message'].widget.attrs.update({'class': 'mb-2'})

    class Meta:
        model = Contact
        fields = '__all__'
