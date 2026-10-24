from django.db import models


class User(models.Model):

    class sextypes(models.IntegerChoices):
        MALE = (1, "Male")
        FEMALE = (2, "Female")
        OTHER = (3, "Other")

    username = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=80)
    birthday = models.DateField(null=False)
    password = models.CharField(max_length=10, blank=False,
                                null=False)
    sex = models.IntegerField(choices=sextypes.choices,
                              default=sextypes.OTHER)
    phone = models.IntegerField()