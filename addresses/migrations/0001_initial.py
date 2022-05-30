# Generated by Django 3.2.5 on 2022-05-30 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.TextField()),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
