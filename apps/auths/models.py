from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, BaseUserManager,)
from django.core.exceptions import ValidationError
from django.utils import timezone
import datetime

# Create your models here.
class ClientManager(BaseUserManager):
    """base client manager class"""

    def create_user(self, email:str, password: str) -> 'Client':
        if not email:
            raise ValidationError("Email is none")

        client: 'Client' = self.model(
            email=self.normalize_email(email),
            password=password
        )
        client.set_password(password)
        client.save(using=self._db)
        return client

    def create_superuser(self, email:str, password: str) -> 'Client':
        if not email:
            raise ValidationError("Email is none")

        client: 'Client' = self.model(
            email=self.normalize_email(email),
            password=password,
        )
        client.is_staff=True
        client.is_superuser=True
        client.set_password(password)
        client.save(using=self._db)
        return client        


class Client(
    AbstractBaseUser,
    PermissionsMixin
):
    """My custom user"""

    email = models.EmailField(
        max_length=100, unique=True, verbose_name='почта'
        )
    is_active = models.BooleanField(
        default=True, verbose_name='активность'
    )
    is_superuser = models.BooleanField(
        default=False, verbose_name='администратор'
    )
    is_staff = models.BooleanField(
        default=False, verbose_name='менеджер'
    )
    date_joined = models.DateTimeField(
        default=timezone.now, verbose_name='дата регистрации'
    )
    balance = models.FloatField(
        default=0.0, verbose_name='баланс'
    )
    born_date = models.DateField(
        auto_now=True, verbose_name='Дата рождения'
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    object = ClientManager()

    class Meta:
        ordering = ('-date_joined',)
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'