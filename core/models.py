from django.contrib.auth.models import AbstractUser
from django.db import models
from companies.models import Company


class User(AbstractUser):
    email = models.EmailField(max_length=255,
                              verbose_name='Электронная почта')

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=60)
    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE,
                                related_name='employees',
                                null=True)

    REQUIRED_FIELDS = ['email', 'first_name',
                       'last_name', 'password']

    def __str__(self):
        return self.username

