from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The email is not given.')
        email = self.normalize_email(email)

        # if not username:
        #     raise ValueError('The username is not given.')
        # username = self.username

        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('SuperUser must have is_staff as True')
        
        if not extra_fields.get('is_superuser'):
            raise ValueError('SuperUser must have is_superuser as True')

        return self.create_user(email, password, **extra_fields)
    
class user(AbstractBaseUser):
    GENDER_CHOICES = (
        (1,'male'),
        (2,'female')
    )
    
    username = models.CharField(max_length = 20, primary_key=True, unique= True)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gender = models.SmallIntegerField(choices= GENDER_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['gender']

    objects = UserManager()

    def __str__(self):
        return self.email
    