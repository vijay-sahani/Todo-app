# Generated by Django 3.1.7 on 2021-03-18 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('Edit_id', models.AutoField(primary_key=True, serialize=False)),
                ('Text', models.TextField(default='', max_length=10000)),
            ],
        ),
    ]
