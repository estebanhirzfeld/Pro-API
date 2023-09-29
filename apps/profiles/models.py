from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from apps.common.models import TimeStampedModel


User = get_user_model()

# Create your models here.

class Profile(TimeStampedModel):
    class Gender(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')
        OTHER = 'O', _('Other')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    gender = models.CharField(verbose_name=_('gender'), max_length=1, choices=Gender.choices, default=Gender.OTHER)
    phone_number = PhoneNumberField(verbose_name=_('phone_number'), max_length=30, blank=True, null=True)
    about_me = models.CharField(verbose_name=_("about me"), max_length=50)
    country = CountryField(verbose_name=_("country"), blank=True, null=True)
    city = models.CharField(verbose_name=_("city"), max_length=50, blank=True, null=True)
    profile_photo = models.ImageField(verbose_name=_("profile photo"), default = "/profile_placeholder.png")

    followers = models.ManyToManyField("self", verbose_name=_("followers"), blank=True, related_name="following", symmetrical=False)

    def __str__(self):
        return f"{self.user.first_name}'s Profile"
    
    def username(self):
        return f"{self.user.first_name}"

    def follow(self, profile):
        self.followers.add(profile)

    def unfollow(self, profile):
        self.followers.remove(profile)

    def check_following(self, profile):
        return self.followers.filter(pkid=profile.pkid).exists()