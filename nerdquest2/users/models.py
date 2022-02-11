from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    address = models.CharField(verbose_name="Address", max_length=100, null=True, blank=True)
    town  = models.CharField(verbose_name="town", max_length=100, null=True, blank=True)
    county = models.CharField(verbose_name="County", max_length=100, null=True, blank=True)
    post_code = models.CharField(verbose_name="Address", max_length=100, null=True, blank=True)
    country= models.CharField(verbose_name="Address", max_length=100, null=True, blank=True)
    longitude= models.CharField(verbose_name="Address", max_length=100, null=True, blank=True)
    lattitude = models.CharField(verbose_name="Address", max_length=100, null=True, blank=True)

    captcha_score = models.FloatField(default= 0.0)
    has_profile = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}'