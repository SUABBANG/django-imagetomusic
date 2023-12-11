from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    user_in_migrations = True
    def create_user(self, email, nickname, password):
        if not email:
            raise ValueError('must have user email')
        if not password:
            raise ValueError('must have user password')
        if not nickname:
            raise ValueError('must have user nickname')
        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname,password):
        user = self.create_user(
            email=self.normalize_email(email),
            nickname=nickname,
            password=password,
        )
        user.is_admin=True
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    object = UserManager()
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    nickname = models.CharField(
        max_length=20,
        null=False,
        unique=True
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'nickname' # nickname 로그인
    REQUIRED_FIELDS = ['email'] # 추가적으로 받을 값

