# Generated by Django 4.2.7 on 2023-12-04 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_resumedata_file_upload'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resumedata',
            old_name='languages1',
            new_name='language1',
        ),
        migrations.RenameField(
            model_name='resumedata',
            old_name='languages2',
            new_name='language2',
        ),
        migrations.RenameField(
            model_name='resumedata',
            old_name='languages3',
            new_name='language3',
        ),
        migrations.RenameField(
            model_name='resumedata',
            old_name='languages4',
            new_name='language4',
        ),
        migrations.RemoveField(
            model_name='resumedata',
            name='file_upload',
        ),
    ]