import uuid
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

# Custom validator function to check for spaces and other invalid characters
def validate_username(value):
    if re.search(r'\s', value):
        raise ValidationError(_("Username cannot contain spaces."))
    if not re.match(r'^[\w.@+-]+$', value):
        raise ValidationError(_("Username contains invalid characters."))


class User(AbstractBaseUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(verbose_name=_("first name"), max_length=50)
    last_name = models.CharField(verbose_name=_("last name"), max_length=50)
    username = models.CharField(
        _("username"),
        max_length=50,
        unique=True,
        validators=[validate_username]  # Add the custom validator here
    )
    email = models.EmailField(
        verbose_name=_("email address"), db_index=True, unique=True
    )
    USERNAME_FIELD = "username"

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(default=timezone.now)


    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        self.username = self.username.lower()  # Convert username to lowercase
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.username

    @property
    def get_full_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"

    @property
    def get_short_name(self):
        return self.first_name