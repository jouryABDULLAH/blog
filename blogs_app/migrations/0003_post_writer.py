# Generated by Django 5.0.3 on 2024-04-25 07:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs_app', '0002_post_written_by'),
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='writer',
            field=models.ForeignKey(default='defaultUser', on_delete=django.db.models.deletion.PROTECT, to='user_app.user'),
        ),
    ]