from django.db import models
import re
# Create your models here.


class UserManager(models.Manager):
    def create_validator(self, post_data):
        errors = {}
        if len(post_data['first_name']) < 2:
            errors['first_name'] = "First Name must be minimum of 2 characters"
        if len(post_data['last_name']) < 2:
            errors['last_name'] = "Last Name must be minimum of 2 characters"
        if len(post_data['email']) < 6:
            errors['email'] = "email must be a minimum of 6 characters"
        if len(post_data['password']) < 6:
            errors['password'] = "Password must be a minimum of 6 characters"
        if len(post_data['password']) != len(post_data['confirm_pw']):
            errors['match'] = "Password and Password confirmation do not match"
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):
            errors['regex'] = "Email is in incorrect format"
        users_with_emails = User.objects.filter(email=post_data['email'])
        if len(users_with_emails) >= 1:
            errors['dup'] = "Email is taken, please use another"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


def __str__(self):
    return f'{self.first_name} {self.last_name}'

    # Create your models here.
class GameManager(models.Manager):
    def create_validator(self, post_data):
        errors = {}
        if len(post_data['gameType']) < 2:
            errors['gameType'] = 'Game type  field should be at least 2 characters'
        if len(post_data['date']) < 0:
            errors['date'] = 'Date is required'

class Game(models.Model):
    gameType = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    startTime = models.TimeField(auto_now=True)
    endTime = models.TimeField(auto_now=False)
    location = models.CharField(max_length=255)
    notes = models.TextField(max_length=2500)
    creator = models.ForeignKey(User, related_name='created_games',on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_name='games')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = GameManager()

    def __str__(self):
        return f"Type of Game: {self.gameType}"
