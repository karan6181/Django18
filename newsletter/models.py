from django.db import models

# Create your models here.

class SignUp(models.Model):
    full_name = models.CharField( max_length=40, blank=False, null=True )
    email = models.EmailField( blank=False, null=True )
    timestamp = models.DateTimeField( auto_now_add=True, auto_now=False )
    updated = models.DateTimeField( auto_now_add=False, auto_now=True )

    def __str__(self):
        return self.email

class ContactUs( models.Model ):
    full_name = models.CharField( max_length=40, blank=False )
    email = models.EmailField(blank=False)
    message = models.TextField()

    def __str__(self):
        return self.full_name