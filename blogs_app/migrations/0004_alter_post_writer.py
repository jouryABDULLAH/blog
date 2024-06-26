# Generated by Django 5.0.3 on 2024-04-25 07:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs_app', '0003_post_writer'),
        ('user_app', '0002_remove_user_id_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user_app.user'),
        ),
    ]
