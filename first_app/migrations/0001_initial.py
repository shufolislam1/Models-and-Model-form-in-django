# Generated by Django 4.2.7 on 2023-12-11 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField(primary_key=True, serialize=False)),
                ('address', models.TextField()),
            ],
        ),
    ]