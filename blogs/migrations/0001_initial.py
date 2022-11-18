# Generated by Django 4.1.2 on 2022-10-23 03:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('content', models.CharField(max_length=2500)),
                ('date_posted', models.DateField(default=django.utils.timezone.now)),
                ('likes', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]