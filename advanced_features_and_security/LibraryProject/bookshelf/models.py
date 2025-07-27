from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self,date_of_birth, profile_photo):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email,date_of_birth)
        user.set_password(None)
        user.save(using=self._db)
        return user

    def create_superuser(self,date_of_birth, profile_photo):
        user = self.create_user(date_of_birth, profile_photo)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
    
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    date_of_birth = models.DateField(null=True, blank=True) 
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    
    objects = CustomUserManager()   
#create customUserManager






# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    def __str__(self):
        return f'Book title: {self.title} by {self.author} ({self.publication_year})'