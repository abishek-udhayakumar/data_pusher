from django.contrib import admin
from .models import Account, Destination

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_id', 'email', 'account_name', 'app_secret_token', 'website')
    search_fields = ('email', 'account_name')
    readonly_fields = ('account_id', 'app_secret_token')

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'url', 'http_method')
    search_fields = ('account__account_name', 'url')
    readonly_fields = ('id',)
