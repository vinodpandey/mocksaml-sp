from typing import Any, Optional

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email: str, password: Optional[str] = None, **extra_fields: Any) -> Any:
        """
        Creates and saves a User with the given username, email and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = UserManager.normalize_email(email)
        user = self.model(email=email, is_staff=False, is_superuser=False, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: Optional[str], **extra_fields: Any) -> Any:
        u = self.create_user(email, password, **extra_fields)
        u.is_staff = True
        u.is_active = True
        u.is_superuser = True
        u.save(using=self._db)
        return u

    def create_staff(self, email: str, password: Optional[str], **extra_fields: Any) -> Any:
        u = self.create_user(email, password, **extra_fields)
        u.is_staff = True
        u.is_active = True
        u.is_superuser = False
        u.save(using=self._db)
        return u


class User(AbstractUser):
    """Custom User model for email-only authentication."""

    email = models.EmailField(unique=True)  # Unique email as login field
    username = None  # Disable username

    USERNAME_FIELD = "email"  # Login with email
    REQUIRED_FIELDS = []  # No required fields beyond email/password

    objects = UserManager()

    # Optional: Auto-set email for display
    def __str__(self):
        return self.email
