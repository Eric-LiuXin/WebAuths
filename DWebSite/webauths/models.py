from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length = 200)
    type = models.CharField(max_length = 200, default = 'trainee')

class UserAuths(models.Model):
    user_id = models.PositiveIntegerField(blank=False)
    identity_type = models.CharField(max_length = 20, default = 'account')
    indentifer = models.CharField(max_length = 20)
    credential = models.CharField(max_length = 20)
