# Generated by Django 4.2.3 on 2023-07-08 21:32

from django.db import migrations, models
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_post_remove_eventphoto_event_delete_event_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='client',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=events.models.upload_to),
        ),
        migrations.AddField(
            model_name='post',
            name='project_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published'), (2, 'Archived')], default=0),
        ),
    ]
