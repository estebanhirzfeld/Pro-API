# Generated by Django 4.1.7 on 2023-09-04 00:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "username",
                    models.CharField(
                        max_length=30, unique=True, verbose_name="username"
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                        default="O",
                        max_length=1,
                        verbose_name="gender",
                    ),
                ),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True,
                        max_length=30,
                        null=True,
                        region=None,
                        verbose_name="phone_number",
                    ),
                ),
                ("about_me", models.CharField(max_length=50, verbose_name="about me")),
                (
                    "country",
                    django_countries.fields.CountryField(
                        blank=True, max_length=2, null=True, verbose_name="country"
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="city"
                    ),
                ),
                (
                    "profile_photo",
                    models.ImageField(
                        default="/profile_placeholder.png",
                        upload_to="",
                        verbose_name="profile photo",
                    ),
                ),
                (
                    "followers",
                    models.ManyToManyField(
                        blank=True,
                        related_name="following",
                        to="profiles.profile",
                        verbose_name="followers",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at", "-updated_at"],
                "abstract": False,
            },
        ),
    ]
