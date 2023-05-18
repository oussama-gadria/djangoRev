from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator, MinLengthValidator, RegexValidator
from django.core.exceptions import ValidationError
# Create your models here.
#class Event 
def is_mail_esprit(value):
    if str(value).endswith('@esprit.tn')==False:
        raise ValidationError("your email must be @esprit.tn")

class Person(AbstractUser):
    cin=models.CharField(
        "CIN",
        primary_key=True,
        max_length=8,
        validators=[
            RegexValidator(
                regex='^[0-9]{8}$',
                message="8 digit only"
            )
        ]
    )
    username=models.CharField("Username ",max_length=255,unique=True)
    email=models.EmailField(
        unique=True, #email unique
        validators=[
           is_mail_esprit
        ]
    )
    USERNAME_FIELD = 'username'
    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural="users"
