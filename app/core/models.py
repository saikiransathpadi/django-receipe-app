"""
Database models
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from utils.models import TimestampModel


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extrafields):
        """Create and return user"""
        user = self.model(email=email, **extrafields)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, TimestampModel, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'