# Generated by Django 4.0.3 on 2022-03-18 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(max_length=50)),
                ('group', models.CharField(max_length=50)),
                ('invite_reason', models.CharField(max_length=64)),
            ],
        ),
    ]