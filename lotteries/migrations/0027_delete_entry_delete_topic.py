# Generated by Django 4.0.4 on 2022-07-24 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lotteries', '0026_remove_plan_contact_contact_remove_plan_contact_plan_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Entry',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]
