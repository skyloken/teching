from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    icon = models.ImageField('アイコン', upload_to='icons/')
    bio = models.CharField('バイオグラフィー', max_length=200)
