from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, user_name, first_name, last_name, password, **other_fields):
        email = self.normalize_email(email)
        
        user = self.model(email=email, user_name=user_name, first_name=first_name,
                          last_name=last_name, **other_fields)
        user.set_password(password)
        user.save()
        return user
        
    def create_superuser(self, user_name, first_name, last_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        
        


class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True, blank=False)
    user_name = models.CharField(max_length = 25, unique=True, blank=False)
    first_name =  models.CharField(max_length = 25, blank=False)
    last_name = models.CharField(max_length = 25, blank=False)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'last_name', "password"]
    
    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.email}, {self.user_name}"