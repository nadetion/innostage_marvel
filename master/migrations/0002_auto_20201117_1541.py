# Generated by Django 3.1.3 on 2020-11-17 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comic',
            old_name='desription',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='image',
            name='file',
        ),
        migrations.AddField(
            model_name='image',
            name='extension',
            field=models.CharField(default='', max_length=255, verbose_name='Расширение'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='path',
            field=models.CharField(default='', max_length=255, verbose_name='Путь'),
            preserve_default=False,
        ),
    ]
