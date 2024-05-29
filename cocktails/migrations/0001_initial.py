# Generated by Django 5.0.6 on 2024-05-28 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('instructions', models.CharField(max_length=500)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]