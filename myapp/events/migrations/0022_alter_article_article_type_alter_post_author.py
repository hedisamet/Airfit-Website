# Generated by Django 4.2.3 on 2023-07-20 22:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0021_post_author_post_project_url_alter_article_links_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_type',
            field=models.CharField(choices=[('books', 'Books'), ('book_chapters', 'Book Chapters'), ('refereed_articles', 'Refereed Articles'), ('conference_papers', 'Conference Papers'), ('phd_thesis', 'PhD Thesis'), ('master_theisis', 'Master Thesis'), ('other_publications', 'Other Publications')], max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
