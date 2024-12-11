import pdb
from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserCreation, Post, Image, Speaker, Article
from django.utils.text import slugify

# Create your tests here.

class UserCreationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='12345'
        )
        self.user_creation = UserCreation.objects.create(
            user=self.user,
            token='testtoken123',
            approved=False
        )

    def test_user_creation_str(self):
        self.assertEqual(str(self.user_creation), 'testuser')

    def test_user_creation_fields(self):
        self.assertEqual(self.user_creation.token, 'testtoken123')
        self.assertFalse(self.user_creation.approved)

    def test_display_user_creation(self):
        # Assertions instead of print statements for automated testing
        self.assertEqual(self.user_creation.user.username, 'testuser')
        self.assertEqual(self.user_creation.token, 'testtoken123')
        self.assertFalse(self.user_creation.approved)

        # Ensure the database contains the expected user creation data
        all_users = UserCreation.objects.all()
        self.assertEqual(all_users.count(), 1)  # Expecting one user creation object
        for user in all_users:
            self.assertEqual(user.user.username, 'testuser')
            self.assertEqual(user.token, 'testtoken123')
            self.assertFalse(user.approved)


class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='12345'
        )
        self.post = Post.objects.create(
            title='Test Post',
            slug=slugify('Test Post'),
            author=self.user
        )

    def test_post_creation(self):
        pdb.set_trace()  # Debugger breakpoint to inspect `self.post`
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.slug, 'test-post')
        self.assertEqual(self.post.author, self.user)

    def test_display_post(self):
        # Assertions for the post details
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.slug, 'test-post')
        self.assertEqual(self.post.author.username, 'testuser')

        # Ensure the database contains the expected post data
        all_posts = Post.objects.all()
        self.assertEqual(all_posts.count(), 1)  # Expecting one post
        for post in all_posts:
            self.assertEqual(post.title, 'Test Post')
            self.assertEqual(post.slug, 'test-post')
            self.assertEqual(post.author.username, 'testuser')


class ImageTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='12345'
        )
        self.post = Post.objects.create(
            title='Test Post',
            slug=slugify('Test Post'),
            author=self.user
        )
        self.image = Image.objects.create(
            post=self.post,
            image='default.jpg'
        )

    def test_image_creation(self):
        self.assertEqual(self.image.post, self.post)
        self.assertEqual(self.image.image, 'default.jpg')

    def test_display_image(self):
        # Assertions for the image details
        self.assertEqual(self.image.post.title, 'Test Post')
        self.assertEqual(self.image.image, 'default.jpg')

        # Ensure the database contains the expected image data
        all_images = Image.objects.all()
        self.assertEqual(all_images.count(), 1)  # Expecting one image
        for img in all_images:
            self.assertEqual(img.post.title, 'Test Post')
            self.assertEqual(img.image, 'default.jpg')


class SpeakerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='12345'
        )
        self.post = Post.objects.create(
            title='Test Post',
            slug=slugify('Test Post'),
            author=self.user
        )
        self.speaker = Speaker.objects.create(
            post=self.post,
            name='Test Speaker',
            description='Test Description'
        )

    def test_speaker_creation(self):
        self.assertEqual(self.speaker.post, self.post)
        self.assertEqual(self.speaker.name, 'Test Speaker')
        self.assertEqual(self.speaker.description, 'Test Description')

    def test_speaker_str(self):
        self.assertEqual(str(self.speaker), 'Test Speaker')

    def test_display_speaker(self):
        # Assertions for the speaker details
        self.assertEqual(self.speaker.name, 'Test Speaker')
        self.assertEqual(self.speaker.description, 'Test Description')

        # Ensure the database contains the expected speaker data
        all_speakers = Speaker.objects.all()
        self.assertEqual(all_speakers.count(), 1)  # Expecting one speaker
        for speaker in all_speakers:
            self.assertEqual(speaker.name, 'Test Speaker')
            self.assertEqual(speaker.description, 'Test Description')


class ArticleTest(TestCase):
    def setUp(self):
        self.article = Article.objects.create(
            title='Test Article',
            article_type='books',
            authors='Test Author',
            publication_date=2023,
            links='https://example.com',
            bibtex='@article{test}'
        )

    def test_article_creation(self):
        pdb.set_trace()  # Debugger breakpoint to inspect `self.article`
        self.assertEqual(self.article.title, 'Test Article')
        self.assertEqual(self.article.article_type, 'books')
        self.assertEqual(self.article.authors, 'Test Author')
        self.assertEqual(self.article.publication_date, 2023)
        self.assertEqual(self.article.links, 'https://example.com')
        self.assertEqual(self.article.bibtex, '@article{test}')

    def test_article_str(self):
        self.assertEqual(str(self.article), 'Test Article')

    def test_display_article_info(self):
        # Incorrect assertion to force failure
        self.assertEqual(self.article.title, 'Wrong Title')  # This will fail
        
        # Ensure the database contains the expected article data
        all_articles = Article.objects.all()
        self.assertEqual(all_articles.count(), 1)  # Expecting one article
        for article in all_articles:
            # These assertions will pass as the article in the database is correct
            self.assertEqual(article.title, 'Test Article')
            self.assertEqual(article.authors, 'Test Author')
            self.assertEqual(article.article_type, 'books')
