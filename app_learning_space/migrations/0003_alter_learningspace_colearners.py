# Generated by Django 4.0.4 on 2022-05-27 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_profile', '0002_alter_profile_profile_picture'),
        ('app_learning_space', '0002_alter_learningspace_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learningspace',
            name='colearners',
            field=models.ManyToManyField(blank=True, to='app_profile.profile'),
        ),
    ]
