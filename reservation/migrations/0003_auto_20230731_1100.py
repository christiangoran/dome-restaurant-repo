# Generated by Django 3.2.20 on 2023-07-31 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_remove_reservation_start_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='image',
        ),
        migrations.AddField(
            model_name='reservation',
            name='customer_email',
            field=models.EmailField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='number_of_seats',
            field=models.IntegerField(default=2),
        ),
    ]