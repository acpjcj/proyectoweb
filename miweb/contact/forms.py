from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', required=True)
    email = forms.EmailField(label='Email', required=True)
    message = forms.CharField(label='Menaje', required=True, widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}))