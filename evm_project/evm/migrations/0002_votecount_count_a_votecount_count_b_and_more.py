# Generated by Django 4.1.13 on 2024-06-25 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='votecount',
            name='count_a',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='votecount',
            name='count_b',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='votecount',
            name='count_c',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='votecount',
            name='count_d',
            field=models.IntegerField(default=0),
        ),
    ]
