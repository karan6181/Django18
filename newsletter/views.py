from django.shortcuts import render

# Create your views here.
from django.db import models
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from .forms import SignUpForm, ContactForm

User = get_user_model()

def home( request ):
    title = "Newsletter SignUp"
    form = SignUpForm( request.POST or None )

    if form.is_valid():
        instance = form.save( commit=False )
        instance.save()
        # print(instance.email)
        # print(instance.full_name)
        # print(instance.timestamp)
    context = {
        "title" : title,
        "form" : form,
    }
    return render( request, "home.html", context )


def contact( request ):
    title = "Contact Us"
    contForm = ContactForm( request.POST or None )
    print(contForm.is_valid())
    if contForm.is_valid():
        # print(form)
        # print(form.cleaned_data)
        # form_email = form.cleaned_data.get( 'email' )
        # form_full_name = form.cleaned_data.get( 'full_name' )
        # form_message = form.cleaned_data.get( 'message' )

        #form.objects.create( form_full_name, form_email,form_message)
        #form.save(commit=True)
        instance1 = contForm.save( commit=False )
        instance1.save()
        return HttpResponseRedirect("/")


        # subject = "Demo Contact form"
        # from_email = settings.EMAIL_HOST_USER
        # to_email = [ from_email, "yourotheremail@email.com" ]
        # contact_message = "%s:%s via %s" %( form_full_name, form_message,
        #                                     form_email )
        #
        # send_mail(subject, contact_message, from_email, [to_email],
        #           fail_silently=True)

    context = {
        "form" : contForm,
        "title" : title,
    }
    return render( request, "forms.html", context )