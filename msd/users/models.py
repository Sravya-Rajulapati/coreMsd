import re

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core import exceptions
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _


class UserAccountManager(BaseUserManager):
    """
    Custom manager for the UserAccount model.

    This manager provides methods for creating user accounts and superuser accounts.

    Args:
        BaseUserManager (class): The base user manager class.

    Methods:
        create_user(email, date_of_birth, password=None, **kwargs): Create a new user account.
        create_superuser(email, password=None, **kwargs): Create a new superuser account.
    """

    def create_user(self, email=None, password=None, mobile_number=None, is_vendor=False, is_staff=False, **kwargs):
        """
        Create and save a new user account with email and password or mobile number.

        Args:
            email (str, optional): The user's email address. Defaults to None.
            password (str, optional): The user's password. Defaults to None.
            mobile_number (str, optional): The user's mobile number. Defaults to None.
            **kwargs: Additional keyword arguments for the user account.

        Returns:
            UserAccount: The created user account.

        Raises:
            exceptions.ValidationError: If both email and mobile number are missing.
            exceptions.ValidationError: If the password does not meet the validation criteria.
        """
        if email is None and mobile_number is None:
            raise exceptions.ValidationError(
                _('Please provide an email address or mobile number.')
            )

        if password is not None:
            self.validate_password(password)

        existing_user = self.get_by_email(email)

        if existing_user:
            return existing_user

        user = self.model(
            email=self.normalize_email(email).lower() if email else None,
            mobile_number=mobile_number,
            is_vendor=is_vendor,
            is_staff=is_staff,
            **kwargs,
        )

        if password is not None:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def get_by_email(self, email):
        try:
            return self.get(email=email)
        except self.model.DoesNotExist:
            return None

    def create_superuser(self, email, password=None, **kwargs):
        """
        Create and save a new superuser account with email and password.

        Args:
            email (str, optional): The superuser's email address. Defaults to None.
            password (str, optional): The superuser's password. Defaults to None.
            **kwargs: Additional keyword arguments for the superuser account.

        Returns:
            UserAccount: The created superuser account.

        Raises:
            exceptions.ValidationError: If the password does not meet the validation criteria.
        """
        if password is not None:
            self.validate_password(password)

        user = self.create_user(
            email=email,
            password=password,
            **kwargs,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def validate_password(self, password):
        """
        Validate the given password to ensure it meets security requirements.

        Args:
            password (str): The password to be validated.

        Raises:
            exceptions.ValidationError: If the password does not meet the validation criteria.
        """
        if len(password) < 8:
            raise exceptions.ValidationError(
                _('The password must be at least 8 characters long.')
            )

        if not any(char.isupper() for char in password):
            raise exceptions.ValidationError(
                _('The password must contain at least one uppercase character.')
            )

        if not any(char.islower() for char in password):
            raise exceptions.ValidationError(
                _('The password must contain at least one lowercase character.')
            )

        if not any(char.isdigit() for char in password):
            raise exceptions.ValidationError(
                _('The password must contain at least one digit.')
            )

        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise exceptions.ValidationError(
                _(
                    'The password must contain at least one special character (e.g., !@#$%^&*()).'
                )
            )


def validate_mobile_number(mobile_number):
    """
    Validate the mobile number.

    Args:
        mobile_number (str): The mobile number to be validated.

    Returns:
        str: The cleaned mobile number.

    Raises:
        exceptions.ValidationError: If the mobile number is invalid.
    """
    # Ensure the mobile number contains only digits
    if not mobile_number.isdigit():
        raise exceptions.ValidationError(_('Mobile number must contain only digits.'))

    # Remove non-digit characters and whitespace from the mobile number
    cleaned_mobile_number = re.sub(r'\D', '', mobile_number)

    return cleaned_mobile_number


class UserAccount(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    """
    Custom user model for the application.

    This model extends AbstractBaseUser and PermissionsMixin to provide custom user authentication.

    Fields:
        first_name (str): The user's first name.
        last_name (str): The user's last name.
        email (str, optional): The user's email address. Defaults to None.
        date_of_birth (date, optional): The user's date of birth. Defaults to None.
        is_active (bool): Whether the user account is active.
        is_staff (bool): Whether the user has staff access.
        is_superuser (bool): Whether the user is a superuser.
        address (str, optional): The user's address. Defaults to None.
        gender (str, optional): The user's gender. Defaults to None.
        profile_picture (ImageField, optional): The user's profile picture. Defaults to None.
        mobile_number (str, optional): The user's mobile number. Defaults to None.
        email_verified (bool): Whether the user's email is verified.
        phone_verified (bool): Whether the user's phone number is verified.
        created_at (datetime): The user's creation date and time.
        location (str): The user's location.
        is_routable (bool): Whether the user's IP address is routable.
        verification_code (str, optional): The verification code for email/phone verification. Defaults to None.
        verification_code_expiry (datetime, optional): The expiration time for the verification code. Defaults to None.
        latitude (Decimal, optional): The user's latitude. Defaults to None.
        longitude (Decimal, optional): The user's longitude. Defaults to None.

    Manager:
        objects (UserAccountManager): The custom manager for this user model.

    Attributes:
        USERNAME_FIELD (str): The field used for username authentication (email).
        REQUIRED_FIELDS (list): List of fields required for user creation.

    Methods:
        __str__(): Return the string representation of the user.
        get_full_name(): Return the full name of the user.
        get_short_name(): Return the short name of the user.
        has_perm(perm, obj=None): Does the user have a specific permission?
        has_module_perms(app_label): Does the user have permissions to view the app `app_label`?
    """

    # Fields, methods, and attributes implementation details
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    address = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True, choices=GENDER_CHOICES)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    mobile_number = models.CharField(
        max_length=15,
        unique=True,
        blank=True,
        null=True,
        validators=[validate_mobile_number],
    )
    email_verified = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=255, default='Unknown')
    is_routable = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=6, blank=True, null=True)
    verification_code_expiry = models.DateTimeField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        """
        Return the email address as the string representation of the user.

        Returns:
            str: The user's email address.
        """
        return self.email

    def get_full_name(self):
        """
        Return the full name of the user.

        Returns:
            str: The user's full name.
        """
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        """
        Return the short name of the user.

        Returns:
            str: The user's short name.
        """
        return self.first_name

    def has_perm(self, perm, obj=None):
        """ Does the user have a specific permission? """
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """ Does the user have permissions to view the app `app_label`? """
        # Simplest possible answer: Yes, always
        return True


class VendorUser(UserAccount):
    """
    Custom user model for vendor users.

    This model extends the UserAccount model to provide additional fields specific to vendor users.

    Fields:
        category (str, optional): The category associated with the vendor user. Defaults to None.
    """
    vendor_name = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)


# def create_custom_permissions():
#     content_type = ContentType.objects.get_for_model(UserAccount)

#     # Permission for custom action
#     custom_action_permission, _ = Permission.objects.get_or_create(
#         codename="can_custom_action",
#         name="Can perform a custom action",
#         content_type=content_type
#     )

#     # Permission for staff-specific action
#     staff_action_permission, _ = Permission.objects.get_or_create(
#         codename="can_staff_action",
#         name="Can perform a staff action",
#         content_type=content_type
#     )

#     # Permission for vendor-specific action
#     vendor_action_permission, _ = Permission.objects.get_or_create(
#         codename="can_vendor_action",
#         name="Can perform a vendor action",
#         content_type=content_type
#     )

# create_custom_permissions()
# normal_user_group, created = Group.objects.get_or_create(name="Normal User")
# vendor_user_group, created = Group.objects.get_or_create(name="Vendor User")
# staff_user_group, created = Group.objects.get_or_create(name="Staff User")
# superuser_group, created = Group.objects.get_or_create(name="Superuser")

# # Assign custom permissions to groups
# custom_action_permission = Permission.objects.get(codename="can_custom_action")
# vendor_action_permission = Permission.objects.get(codename="can_vendor_action")
# staff_action_permission = Permission.objects.get(codename="can_staff_action")

# normal_user_group.permissions.add(custom_action_permission)
# vendor_user_group.permissions.add(custom_action_permission, vendor_action_permission)
# staff_user_group.permissions.add(custom_action_permission, staff_action_permission)
