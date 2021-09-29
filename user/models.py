from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from common.models import TimeModel

class UserManager(BaseUserManager):
    def create_user(self, mobile, password=None, is_admin=False, is_staff=False, is_active=True):
        if not mobile:
            raise ValueError("User must have a mobile")
        user = self.model(
            mobile=mobile
        )
        user.set_password(password)  # change password to hash
        user.is_admin = is_admin
        user.username = mobile
        user.is_staff = is_staff
        user.is_active = is_active
        user.save(using=self._db)
        return user
        
    def create_superuser(self, mobile, password=None, **extra_fields):
        user = self.model(
            mobile=mobile
        )
        user.set_password(password)
        user.is_admin = True
        user.username = mobile
        user.mobile= mobile
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_staffuser(self, mobile, password=None):
        user = self.create_user(
            full_name,
            profile_picture,
            gender,
            password=password,
            is_staff=True,
        )
        return user

class User(AbstractUser, TimeModel):
    mobile = models.CharField(max_length=12, unique=True)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)


    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELD = ['mobile']
    objects = UserManager()

    def save(self,*args,**kwargs):
        if not self.username:
            self.username = self.mobile
            self.set_password(self.password)
        super(User, self).save(*args,**kwargs)

class Group(TimeModel):
    name = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

class GroupUser(TimeModel):
    group = models.ForeignKey(Group, related_name='group', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='group_user', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.group}: {self.user}'



