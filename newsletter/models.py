from django.db import models

# Create your models here.
class SignUp(models.Model):
    email = models.EmailField()
    firstname = models.CharField(max_length=120, blank=True, null=True)
    full_name = models.CharField(max_length=120, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated =  models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):  #python 3.3 is __str__
        return self.email

