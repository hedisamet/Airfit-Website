from django.db import models
from django.contrib.auth.models import User


def upload_to(instance, filename):
    if hasattr(instance, 'slug'):
        if isinstance(instance, Article):
            return f'documents/{instance.slug}/{filename}'
        elif isinstance(instance, Image):
            return f'images/{instance.slug}/{filename}'
    if isinstance(instance, Article):
        return f'documents/default/{filename}'
    elif isinstance(instance, Image):
        return f'images/default/{filename}'


class UserCreation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=32)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


STATUS = (
    (0, 'Draft'),
    (1, 'Published'),
    (2, 'Archived'),
)

ARTICLE_TYPES = (
    ('books', 'Books'),
    ('book_chapters', 'Book Chapters'),
    ('refereed_articles', 'Refereed Articles'),
    ('conference_papers', 'Conference Papers'),
    ('phd_thesis', 'PhD Thesis'),
    ('master_theisis', 'Master Thesis'),
    ('other_publications', 'Other Publications'),
)





class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    presentation = models.TextField()
    event_date = models.DateField(null=True)
    program_image = models.ImageField(upload_to="event_program_images/", null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_images')
    image = models.ImageField(upload_to="images/", default='default.jpg')


class Speaker(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='speakers')
    name = models.CharField(max_length=200)
    description = models.TextField(default='Default')

    def __str__(self):
        return self.name




class Article(models.Model):
    title = models.CharField(max_length=200, null=True)
    article_type = models.CharField(max_length=200, choices=ARTICLE_TYPES)
    authors = models.CharField(max_length=200, null=True)
    publication_date = models.IntegerField(null=True)
    document = models.FileField(upload_to=upload_to, null=True, blank=True)
    links = models.URLField(blank=True)
    bibtex = models.TextField(blank=True)

    def __str__(self):
        return self.title

    