# Generated by Django 4.2.7 on 2023-12-04 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_resumedata_skill_label1_resumedata_skill_label2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumedata',
            name='skill_percent1',
            field=models.IntegerField(default=0),
        ),
    ]
