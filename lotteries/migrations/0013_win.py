# Generated by Django 4.0.4 on 2022-05-20 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lotteries', '0012_delete_win'),
    ]

    operations = [
        migrations.CreateModel(
            name='Win',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scan_date', models.DateField(auto_now_add=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotteries.player')),
            ],
            options={
                'verbose_name_plural': 'Wins',
            },
        ),
    ]
