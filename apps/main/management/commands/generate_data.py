from typing import Any
from datetime import datetime
from django.core.management.base import BaseCommand
from main.models import (Player, Team, Stadium)
import random
import names
import requests
from requests.models import Response


url = "https://gist.githubusercontent.com/jamesmwali/11b34a6d4c87644915573e54fbd34ac5/raw/93124e101231f8cbf14ff48ca191156059d6c41f/playerlist.json"
r: Response = requests.get(url)
data = r.json()

team = []
for element in data:
    team.append(element.get("team"))
teams = set(team)


class Command(BaseCommand):
    """Custom command for filling up database"""

    help = 'Custom command for filling up database'

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        pass

    def generate_players(self) -> None:

        # PLAYERS_COUNT: int = 250
        MAX_POWER: int = 99
        MIN_POWER: int = 30
        MAX_AGE: int = 40
        MIN_AGE: int = 17
        
        res = Player.objects.count()
        sum = len(data) - res
        if res < sum:
            for element in data:
                try:
                    Player.objects.create(
                        name=element.get("first_name"),
                        last_name=element.get("last_name"),
                        power=random.randrange(MIN_POWER, MAX_POWER),
                        age=random.randrange(MIN_AGE, MAX_AGE)
                    )
                except:
                    Player.objects.create(
                        name=names.get_first_name(gender='Male'),
                        last_name=element.get("last_name"),
                        power=random.randrange(MIN_POWER, MAX_POWER),
                        age=random.randrange(MIN_AGE, MAX_AGE)
                    )
        print("Хватит уже игроков")

    def generate_stadium(self) -> None:

        STADIUM_COUNT: int = 19
        MAX_SIZE: int = 99
        MIN_SIZE: int = 30
        
        _: int
        res = Stadium.objects.count()
        sum = STADIUM_COUNT - res
        if res < STADIUM_COUNT:
            for _ in range(sum):
                Stadium.objects.create(
                    name=names.get_first_name(gender='male'),
                    city=names.get_last_name(),
                    perimetr=random.randint(MIN_SIZE, MAX_SIZE)
                )
        print('хватит уже стадионов')

    def generate_teams(self) -> None:

        TEAMS_COUNT: int = 19
        PLAYERS: int = 11

        res = Team.objects.count()
        sum = len(data) - res
        if res < sum:
            for i in teams:
                Team.objects.create(
                    title=i
                )
        print("хватит уже команд")

    def handle(self, *args: Any, **kwargs: Any) -> None:
        """Handles data filling."""

        start: datetime = datetime.now()
        self.generate_stadium()
        self.generate_teams()
        self.generate_players()
        print(
            f'Generated in: {(datetime.now() - start).total_seconds()}'
        )