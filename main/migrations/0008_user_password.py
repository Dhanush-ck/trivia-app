# Generated by Django 5.2.1 on 2025-05-21 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='0000', max_length=16),
        ),
    ]
