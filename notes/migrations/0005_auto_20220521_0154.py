# Generated by Django 2.1.15 on 2022-05-21 01:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_notes_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to=settings.AUTH_USER_MODEL),
        ),
    ]
