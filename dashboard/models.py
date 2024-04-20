from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    date_joined = None

    id = models.CharField(primary_key=True, default=uuid.uuid4(), max_length=36)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(unique=True, max_length=100)
    email = models.CharField(unique=True, max_length=200)
    phone = models.CharField(unique=True, max_length=15)
    password = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    @classmethod
    def email_exists(cls, email):
        return cls.objects.filter(email=email).exists()

    class Meta:
        db_table = 'user'


class UserRoomLink(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4(), max_length=36)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_room_link_user')
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_room_link'
