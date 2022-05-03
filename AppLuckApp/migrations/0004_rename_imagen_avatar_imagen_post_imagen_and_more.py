# Generated by Django 4.0.3 on 2022-05-03 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppLuckApp', '0003_alter_post_fecha_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avatar',
            old_name='Imagen',
            new_name='imagen',
        ),
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='blogpics'),
        ),
        migrations.AlterField(
            model_name='post',
            name='contenido',
            field=models.CharField(max_length=3000),
        ),
    ]