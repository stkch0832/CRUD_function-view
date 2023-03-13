from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('メールアドレスを入力してください')
        user = self.model(
            email=email,
        )
        user.set_password(password)
        user.save(usin=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.model(
            email=email,
        )
        user.set_password(password)
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.email


