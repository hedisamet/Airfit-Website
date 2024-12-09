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
        print("\n=== User Creation Details ===")
        print(f"Username: {self.user_creation.user.username}")
        print(f"Token: {self.user_creation.token}")
        print(f"Approved: {self.user_creation.approved}")
        
        print("\n=== All UserCreations in Database ===")
        all_users = UserCreation.objects.all()
        for user in all_users:
            print(f"\nUser: {user.user.username}")
            print(f"Token: {user.token}")
            print(f"Approved: {user.approved}")

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
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.slug, 'test-post')
        self.assertEqual(self.post.author, self.user)

    def test_display_post(self):
        print("\n=== Post Details ===")
        print(f"Title: {self.post.title}")
        print(f"Slug: {self.post.slug}")
        print(f"Author: {self.post.author}")
        
        print("\n=== All Posts in Database ===")
        all_posts = Post.objects.all()
        for post in all_posts:
            print(f"\nPost: {post.title}")
            print(f"Slug: {post.slug}")
            print(f"Author: {post.author}")

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
        print("\n=== Image Details ===")
        print(f"Post: {self.image.post.title}")
        print(f"Image Path: {self.image.image}")
        
        print("\n=== All Images in Database ===")
        all_images = Image.objects.all()
        for img in all_images:
            print(f"\nImage: {img.post.title}")
            print(f"Image Path: {img.image}")

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
        print("\n=== Speaker Details ===")
        print(f"Name: {self.speaker.name}")
        print(f"Description: {self.speaker.description}")
        
        print("\n=== All Speakers in Database ===")
        all_speakers = Speaker.objects.all()
        for speaker in all_speakers:
            print(f"\nSpeaker: {speaker.name}")
            print(f"Description: {speaker.description}")

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
        self.assertEqual(self.article.title, 'Test Article')
        self.assertEqual(self.article.article_type, 'books')
        self.assertEqual(self.article.authors, 'Test Author')
        self.assertEqual(self.article.publication_date, 2023)
        self.assertEqual(self.article.links, 'https://example.com')
        self.assertEqual(self.article.bibtex, '@article{test}')

    def test_article_str(self):
        self.assertEqual(str(self.article), 'Test Article')

    def test_display_article_info(self):
        # Print the created article details
        print("\n=== Created Article Details ===")
        print(f"Title: {self.article.title}")
        print(f"Type: {self.article.article_type}")
        print(f"Authors: {self.article.authors}")
        print(f"Publication Date: {self.article.publication_date}")
        print(f"Links: {self.article.links}")
        print(f"BibTeX: {self.article.bibtex}")
        
        # Display all articles in the database
        print("\n=== All Articles in Database ===")
        all_articles = Article.objects.all()
        for article in all_articles:
            print(f"\nArticle: {article.title}")
            print(f"Authors: {article.authors}")
            print(f"Type: {article.article_type}")
