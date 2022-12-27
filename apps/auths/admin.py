from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.core.handlers.wsgi import WSGIRequest
from typing import Optional, Any

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
                'is_active',
                'born_date'
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
        'born_date'
    ]
    ordering = ('email',)

    def get_readonly_fields(self, request: WSGIRequest, obj: Optional[Client] = None):
        if not obj:
            return self.readonly_fields

        return self.readonly_fields + ('email',)

    def has_add_permission(self, request: WSGIRequest) -> bool:
        return True

    def has_change_permission(self, request: WSGIRequest, obj: Any=None) -> bool:
        return True

    def has_delete_permission(self, request: WSGIRequest, obj: Any=None) -> bool:
        return True

admin.site.register(Client, ClientAdmin)