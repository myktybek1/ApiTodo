# Generated by Django 3.2 on 2021-04-14 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(max_length=250)),
                ('completed', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]
