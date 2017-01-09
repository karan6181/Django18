from django.contrib import admin

# Register your models here.

from .models import SignUp, ContactUs
from .forms import SignUpForm, ContactForm

class SignUpAdmin( admin.ModelAdmin ):
    list_display = [ "full_name", "__str__", "timestamp", "updated" ]
    form = SignUpForm
    # class Meta:
    #     model = SignUp

admin.site.register( SignUp, SignUpAdmin )

class ContactAdmin( admin.ModelAdmin ):
    list_display = [ "full_name", "email" ]
    form = ContactForm

admin.site.register( ContactUs, ContactAdmin )