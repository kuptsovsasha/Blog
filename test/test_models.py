from django.test import TestCase

# Create your tests here.

from home_page.models import Post

class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Post.objects.create()

    def test_h1(self):
        author = Post.objects.get(id=1)
        max_length = author._meta.get_field('h1').max_length
        self.assertEqual(max_length,200)








