
from django.db import models
from django.utils.crypto import get_random_string

def generate_unique_account_id():
    return get_random_string(20)

class Account(models.Model):
    email = models.EmailField(unique=True)
    account_id = models.CharField(max_length=50, unique=True)
    account_name = models.CharField(max_length=100)
    # app_secret_token = models.CharField(max_length=50, default=get_random_string)
    app_secret_token = models.CharField(max_length=50, default=lambda: get_random_string(50))

    website = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.app_secret_token:
            self.app_secret_token = get_random_string(50)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.account_name

class Destination(models.Model):
    account = models.ForeignKey(Account, related_name='account_destinations', on_delete=models.CASCADE)
    url = models.URLField()
    http_method = models.CharField(max_length=10)
    headers = models.JSONField()

    def __str__(self):
        return self.url
