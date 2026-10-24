from django.db import models


class User(models.Model):

    class sextypes(models.IntegerField):
        MALE = 1
        FEMALE = 2
        OTHER = 3

    username = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=80)
    birthdate = models.DateField(null=False)
    password = models.CharField(max_length=10, blank=False,
                                null=False)
    sex = models.integerField(choices=sextypes.choices,
                              default=sextypes.OTHER)
    phone = models.IntegerField()