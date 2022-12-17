from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.core.handlers.wsgi import WSGIRequest
from typing import Optional

from main.models import Player, Stadium, Team

# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    """PlayerAdmin"""

    model = Player

    # readonly_fields = (
    #     'name',
    #     'last_name'
    # )
    list_display = (
        'name',
        'last_name',
        'power'
    )


class TeamAdmin(admin.ModelAdmin):
    """TeamAdmin"""

    model = Team

    # readonly_fields = (
    #     'title',
    # )
    list_display = (
        'title',
    )

    def get_readonly_fields(self, request: WSGIRequest, obj: Optional[Team] = None):
        if not obj:
            return self.readonly_fields

        return self.readonly_fields + ('title')


class StadiumAdmin(admin.ModelAdmin):
    """StadiumAdmin"""

    model = Stadium

    # readonly_fields = (
    #     'name',
    #     'city'
    # )
    list_display = (
        'name',
        'city',
        'perimetr'
    )


admin.site.register(Player, PlayerAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Stadium, StadiumAdmin)    