# Generated by Django 5.1.2 on 2024-11-16 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0004_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='desc',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]