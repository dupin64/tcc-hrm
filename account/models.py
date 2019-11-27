from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, email, name, password):
        """
        Creates a user with the given email, name and password.
        """
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """
        Creates a superuser.
        """
        user = self.create_user(
            email,
            name=name,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(unique=True, max_length=255)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_receptionist = models.BooleanField(default=False)
    is_specialist = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin or self.is_receptionist

    @property
    def user_type(self):
        if self.is_patient:
            return 'patient'
        elif self.is_specialist:
            return 'specialist'
        elif self.is_receptionist:
            return 'receptionist'


class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Specialist(models.Model):
    title = models.CharField(max_length=255, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Receptionist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
