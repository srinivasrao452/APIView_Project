# Generated by Django 2.0.5 on 2020-02-07 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eno', models.IntegerField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=30)),
                ('esal', models.IntegerField()),
            ],
        ),
    ]