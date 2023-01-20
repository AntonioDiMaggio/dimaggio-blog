from django.test import TestCase
from .models import Post


class ModelTesting(TestCase):
    def setUp(self):
        self.blog = Post.objects.create(title="django", author="django", slug="django")

    def test_post_model(self):
        data = self.blog
        self.assertTrue(isinstance(data, Post))
        self.assertEqual(str(data), "django")
