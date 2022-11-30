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
        
    def create_superuser(self, email, user_name, first_name, last_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        
        return self.create_user(email, user_name, first_name, last_name, password, **other_fields)
        
        


class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True, blank=False)
    user_name = models.CharField(max_length = 25, unique=True, blank=False)
    first_name =  models.CharField(max_length = 25, blank=False)
    last_name = models.CharField(max_length = 25, blank=False)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'last_name']
    
    def __str__(self):
        return f"id: {self.id}, first_name: {self.first_name}, last_name: {self.last_name}, email: {self.email}, user_name: {self.user_name}"
        # return f"id: {self.id}, firstname: {self.first_name}, lastname: {self.last_name}, email: {self.email}, username: {self.user_name}, staff: {self.is_staff}, superuser: {self.is_superuser}"