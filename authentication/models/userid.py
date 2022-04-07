from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class ManageUser(BaseUserManager):
    def create_user(self, username, password=None):
        """
        function that creates and saves an username with a 
        password and an username provided by the user. 
        """
        if not username:
            raise ValueError('Ingrese un nombre de usuario')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

def create_superuser(self, username, password):
    """
    function that creates and saves a superuser
    """
    user = self.create_superuser(
        username=username,
        password=password,
    )
    user.is_admin = True
    user.save(using = self._db)
    return user

class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField('Name', max_length = 15)
    surname = models.CharField('Surname', max_length = 15)
    username = models.CharField('Username', max_length = 15, unique=True)
    password = models.CharField('Password', max_length = 256)
    email = models.EmailField('Email', max_length = 100)

    def save(self, **kwargs):
        shuffling = 'gnrgneofwncjjnjsndsdfj'
        self.password = make_password(self.password, shuffling)
        super().save(**kwargs)

    objects = ManageUser()
    USERNAME_FIELD = 'username'


 