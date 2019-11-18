from django import forms

# our new form
class ContactForm(forms.Form):
    contact_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': ' Email', 'style': 'border-color: #f1f1f1;width:100%; border-radius:10px;'}), label='')
    