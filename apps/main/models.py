from django.db import models

# Create your models here.
class Stadium(models.Model):
    """Stadium"""

    name = models.CharField(
        max_length=20,
        verbose_name='name'
    )
    city = models.CharField(
        max_length=30,
        verbose_name='city'
    )
    perimetr = models.IntegerField(
        verbose_name='size_stadium'
    )

    class Meta:
        ordering = (
            '-perimetr',
        )
        verbose_name = 'стадион'
        verbose_name_plural = 'стадионы'
    
    def __str__(self) -> str:
        return self.name


class Team(models.Model):
    """Team"""

    title = models.CharField(
        max_length=25,
        verbose_name='title'
    )
    stadium = models.ForeignKey(
        Stadium,
        on_delete=models.PROTECT,
        verbose_name='stadium',
        null=True,
        blank=True
    )
    
    class Meta:
        ordering = (
            '-id',
        )
        verbose_name = 'team'
        verbose_name_plural = 'teams'

    def __str__(self) -> str:
        return f'{self.title}'


class Player(models.Model):
    """Player entity."""

    name = models.CharField(
        max_length=25, 
        verbose_name='name'
        )
    last_name = models.CharField(
        max_length=25,
        verbose_name='last_name'
    )
    power = models.IntegerField(
        verbose_name='power'
    )
    age = models.IntegerField(
        verbose_name='age'
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.PROTECT,
        verbose_name='team',
        null=True,
        blank=True
    )

    class Meta:
        ordering = (
            '-power',
        )
        verbose_name = 'player'
        verbose_name_plural = 'players'

    def __str__(self) -> str:
        return f'{self.name} {self.last_name} | {self.power}'
