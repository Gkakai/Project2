# Generated by Django 5.1.2 on 2024-11-15 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agent',
            old_name='title',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='description',
        ),
        migrations.AddField(
            model_name='agent',
            name='image',
            field=models.FileField(default='', upload_to='agents/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='position',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]