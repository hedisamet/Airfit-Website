# Generated by Django 4.2.3 on 2023-07-21 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0024_rename_project_date_post_event_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='speacker',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
