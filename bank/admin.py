from django.contrib import admin
from .models import Client, Account


class ClientAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name"]


admin.site.register(Client, ClientAdmin)
admin.site.register(Account)
