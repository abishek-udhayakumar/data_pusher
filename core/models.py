# Importing the uuid module for generating UUIDs
import uuid
# Importing the models module from django.db
from django.db import models

# Defining the Account model
class Account(models.Model):
    # UUIDField for unique account ID (primary key)
    account_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # EmailField for email address (unique)
    email = models.EmailField(unique=True)
    # CharField for account name
    account_name = models.CharField(max_length=255)
    # CharField for app secret token (unique, default generated using uuid.uuid4)
    app_secret_token = models.CharField(max_length=255, unique=True, default=uuid.uuid4)
    # URLField for website (optional)
    website = models.URLField(blank=True, null=True)

    # String representation of the Account model
    def __str__(self):
        return self.account_name

# Defining the Destination model
class Destination(models.Model):
    # ForeignKey to Account model (related name: destinations)
    account = models.ForeignKey(Account, related_name='destinations', on_delete=models.CASCADE)
    # URLField for destination URL
    url = models.URLField()
    # CharField for HTTP method (e.g., GET, POST, PUT)
    http_method = models.CharField(max_length=10)
    # JSONField for headers (multiple values)
    headers = models.JSONField()

    # String representation of the Destination model
    def __str__(self):
        return self.url
