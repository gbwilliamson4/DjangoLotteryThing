# Generated by Django 4.0.4 on 2022-06-04 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lotteries', '0022_alter_checkscan_scan_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player_guesses',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotteries.player'),
        ),
    ]
