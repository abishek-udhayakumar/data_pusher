from django.contrib import admin
from .models import Account, Destination

# Customizes the admin interface for the Account model
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    # Specifies the fields to display in the list view of the admin interface
    list_display = ('account_id', 'email', 'account_name', 'app_secret_token', 'website')
    # Enables searching for records based on specified fields in the admin interface
    search_fields = ('email', 'account_name')
    # Specifies fields that should be read-only in the admin interface
    readonly_fields = ('account_id', 'app_secret_token')

# Customizes the admin interface for the Destination model
@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    # Specifies the fields to display in the list view of the admin interface
    list_display = ('id', 'account', 'url', 'http_method')
    # Enables searching for records based on specified fields in the admin interface
    search_fields = ('account__account_name', 'url')
    # Specifies fields that should be read-only in the admin interface
    readonly_fields = ('id',)
