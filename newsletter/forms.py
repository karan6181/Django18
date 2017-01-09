from django import forms
from .models import SignUp, ContactUs

class SignUpForm( forms.ModelForm ):
    class Meta:
        model = SignUp
        fields = [ 'full_name', 'email' ]

    def clean_email(self):
        email = self.cleaned_data.get( 'email' )
        email_base, provider = email.split( "@" )
        domain, extension = provider.split( "." )
        if extension != "edu":
            raise forms.ValidationError( "Please use a school(.EDU) email address" )
        return email

class ContactForm( forms.ModelForm ):
    class Meta:
        model = ContactUs
        fields = ["full_name", "email", "message"]
