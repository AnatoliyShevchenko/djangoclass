from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.core.handlers.wsgi import WSGIRequest
from typing import Optional

from main.models import Player, Stadium, Team

# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    """PlayerAdmin"""

    model = Player

    list_display = (
        'name',
        'last_name',
        'power',
        'team'
    )

    def get_readonly_fields(self, request: WSGIRequest, obj: Optional[Player] = None):
        if not obj:
            return self.readonly_fields

        return self.readonly_fields + ('name', 'last_name')


class TeamAdmin(admin.ModelAdmin):
    """TeamAdmin"""

    model = Team

    list_display = (
        'title',
        'stadium',
    )

    # def get_readonly_fields(self, request: WSGIRequest, obj: Optional[Team] = None):
    #     if not obj:
    #         return self.readonly_fields

    #     return self.readonly_fields + ('title')


class StadiumAdmin(admin.ModelAdmin):
    """StadiumAdmin"""

    model = Stadium

    list_display = (
        'name',
        'city',
        'perimetr'
    )
    def get_readonly_fields(self, request: WSGIRequest, obj: Optional[Stadium] = None):
        if not obj:
            return self.readonly_fields

        return self.readonly_fields + ('name','city')


admin.site.register(Player, PlayerAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Stadium, StadiumAdmin)    