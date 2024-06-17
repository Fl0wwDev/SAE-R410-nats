# Generated by Django 5.0.6 on 2024-06-13 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlightDeparture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.CharField(max_length=50)),
                ('departure_time', models.DateTimeField()),
                ('destination', models.CharField(max_length=100)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sieges_disponible', models.PositiveIntegerField(default=100)),
            ],
        ),
    ]