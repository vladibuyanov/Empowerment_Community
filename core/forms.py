from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'NAME'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'EMAIL'}))
    feedback = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'WRITE YOUR FEEDBACK'}))
