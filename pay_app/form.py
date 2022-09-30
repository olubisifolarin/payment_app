from email import message
from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    fullname = forms.CharField( widget=forms.TextInput(attrs={ 'label': 'Full Name', 'placeholder': 'Enter your full name'}))
    amount = forms.IntegerField( widget=forms.TextInput(attrs={ 'label': 'Amount', 'placeholder': 'Enter amount'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        
        'placeholder': 'Enter your email',
        'label': 'Email',
        'id': 'usercomment',
            }))
    class Meta():
        model = Payment
        fields = ['fullname', 'email', 'amount']
        
