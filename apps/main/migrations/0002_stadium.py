# Generated by Django 4.1.3 on 2022-12-14 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stadium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='name')),
                ('city', models.CharField(max_length=30, verbose_name='city')),
                ('perimetr', models.IntegerField(verbose_name='size_stadium')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.team', verbose_name='team')),
            ],
            options={
                'verbose_name': 'Стадион',
                'verbose_name_plural': 'Стадионы',
                'ordering': ('-perimetr',),
            },
        ),
    ]
