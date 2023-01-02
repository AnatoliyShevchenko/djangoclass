from typing import Any
from datetime import datetime
from django.core.management.base import BaseCommand
from main.models import (Player, Team, Stadium)
import random
import names
import requests
from requests.models import Response


class Command(BaseCommand):
    """Custom command for filling up database"""

    help = 'Custom command for filling up database'

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        pass

    def generate_teams_and_stadiums(self) -> None:

        countries_url: str = (
            'https://raw.githubusercontent.com/annexare/Countries/master/data/'
            'countries.json'
        )
        clubs_url: str = (
            'https://raw.githubusercontent.com/openfootball/football.json/maste'
            'r/2020-21/{}.1.clubs.json'
        )
        leagues: tuple[str, ...] = (
            'en',
            'es',
            'it'
        )
        country_objs: dict[str, Any] = requests.get(countries_url).json()
        countries: dict[str, dict[str, Any]] = {}
        _: str
        data: dict[str, Any]
        for _, data in country_objs.items():
            countries[data['name']] = data['capital']

        league: str
        for league in leagues:
            url: str = clubs_url.format(league)

            response: Response = requests.get(url)
            if response.status_code != 200:
                print('Error')
                return

            data: dict[str, str | list[dict[str, str]]] = response.json()
            obj: dict[str, str]
            for obj in data['clubs']:
                capital: str = countries.get(
                    obj['country'],
                    'Unknown'
                )
                stadium: Stadium
                _: bool
                stadium, _ = Stadium.objects.get_or_create(
                    name=f'{obj["code"]} Stadium',
                    perimetr=random.randrange(
                        100,
                        1000,
                        50
                    ),
                    city=capital
                )
                team : Team
                _: bool
                team, _ = Team.objects.get_or_create(
                    title=obj['name'],
                    stadium=stadium
                )
                for j in range(11):
                    Player.objects.get_or_create(
                        name=names.get_first_name(gender='male'),
                        last_name=names.get_last_name(),
                        power=random.randrange(30, 99),
                        age=random.randrange(17, 40),
                        team=team,
                    )


    def handle(self, *args: Any, **kwargs: Any) -> None:
        """Handles data filling."""

        start: datetime = datetime.now()
        self.generate_teams_and_stadiums()
        print(
            f'Generated in: {(datetime.now() - start).total_seconds()}'
        )