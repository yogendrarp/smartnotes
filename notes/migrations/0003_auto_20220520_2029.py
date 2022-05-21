# Generated by Django 2.1.15 on 2022-05-20 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_remove_notes_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='text',
            field=models.TextField(default='Add some notes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notes',
            name='title',
            field=models.CharField(default='Add notes', max_length=200),
            preserve_default=False,
        ),
    ]
