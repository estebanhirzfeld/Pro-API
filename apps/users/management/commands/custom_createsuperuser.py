from django.contrib.auth.management.commands import createsuperuser
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from apps.users.models import validate_username
import getpass

class Command(createsuperuser.Command):
    help = "Create a superuser with a username field."

    def handle(self, *args, **options):
        User = get_user_model()

        # Prompt the user to enter a username
        while True:
            username = input("Enter a username: ").strip()

            # Check if the username is provided and not empty
            if not username:
                self.stderr.write(self.style.ERROR("Username cannot be empty."))
                continue  # Retry the input

            # Use the validate_username function to validate the username
            try:
                validate_username(username)
            except ValidationError as e:
                self.stderr.write(self.style.ERROR(str(e)))
                continue  # Retry the input

            break  # Exit the loop when a valid username is provided

        email = input("Enter an email address: ").strip()
        first_name = input("Enter your first name: ").strip()
        last_name = input("Enter your last name: ").strip()

        while True:
            password = getpass.getpass("Password: ")
            password2 = getpass.getpass("Password (again): ")

            if password != password2:
                self.stderr.write(self.style.ERROR("Passwords do not match."))
                continue

            if len(password) < 8:
                self.stderr.write(self.style.ERROR("Password is too short. It must contain at least 8 characters."))
                continue

            break

        try:
            # Call create_superuser method directly with the required arguments
            User.objects.create_superuser(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password  # Set the password obtained securely
            )
        except ValidationError as e:
            self.stderr.write(self.style.ERROR(str(e)))
