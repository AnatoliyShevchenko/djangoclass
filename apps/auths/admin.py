from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from auths.models import Client


class ClientAdmin(UserAdmin):
    model = Client
    fieldsets = (
        ('Information', {
            'fields': (
                'email',
                'password',
                'date_joined',
            )
        }),
        ('Permissions', {
            'fields': (
                'is_superuser',
                'is_staff',
                'is_active',
            )
        }),
    )
    add_fieldsets = (
        ('Add', {
            'classes': (
                'wide',
            ),
            'fields': (
                'email',
                'password1',
                'password2',
                'is_active'
            )
        }),
    )
    search_fields = ('email',)
    readonly_fields = (
        'date_joined',
        'is_superuser',
        'is_active',
        'is_staff'
        )
    list_filter = (
        'email',
        'is_superuser',
        'is_staff',
        'is_active'
    )
    list_display = [
        'email',
        'password',
        'date_joined',
        'is_superuser',
        'is_staff',
        'is_active',
        # 'born_date'
    ]
    ordering = ('email',)

admin.site.register(Client, ClientAdmin)