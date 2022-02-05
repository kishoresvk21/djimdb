import os.path
import random

from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from .validators import DomainUnicodeusernameValidator,DomainUnicodenameValidator,DomainUnicodemobileValidator
from .managers import CustomUserManager
from django.conf import settings
from django.utils import timezone
# Create your models here.

# def get_filename_ext(filename):
#     base_name=os.path.basename(filename)
#     name,ext=os.path.splitext(filename)
#     return name,ext

# def upload_to(instance,filename):
#     print(instance)
#     print(filename)
#     new_filename=random.randint(1,389999211)
#     name,ext=get_filename_ext(filename)
#     final_filename=f'{new_filename}{ext}'
#     return f"media/userprofile/{final_filename}"

def nameFile(instance, filename):
    return '/'.join(['images', str(instance.username), filename])

# def

class CustomUser(AbstractBaseUser):
    username = models.CharField(_('username'),unique=True,max_length=30,null=False)
    email = models.EmailField(_('email address'), unique=True)
    firstname=models.CharField(_('firstname'),max_length=40)
    lastname=models.CharField(_('lastname'),max_length=30)
    mobile=models.CharField(_('mobile'),max_length=10)
    image=models.ImageField(_("image"),upload_to=nameFile,blank=True)
    # generes=models.TextField(_('generes'),default=None)
    created_at=models.TimeField(auto_now_add=True)
    updated_at=models.TimeField(auto_now=True)
    is_staff=models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','firstname','lastname','mobile']

    objects = CustomUserManager()
    class Meta:
        db_table='users'

    def __str__(self):
        return str(self.username)

    def has_perm(self, perm, obj=None): return self.is_superuser
    def has_module_perms(self, app_label): return True

class UserWishlist(models.Model):
    pass


class MovieProfile(models.Model):
    pass