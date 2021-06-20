from django.contrib.auth import get_user_model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


User = get_user_model()


class ProfileCustomer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_customer')
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    bio = models.CharField(max_length=100, blank=True)
    phone = PhoneNumberField(blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        to_slug = str(self.user.username)
        self.slug = to_slug
        super().save(*args, **kwargs)