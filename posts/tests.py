from django.http import response
from django.test import TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.

class PostModelTest(TestCase):

    def setUp(self) -> None:
        Post.objects.create(content='Hello, Test!')
    
    def test_content(self) -> None:
        post = Post.objects.get(id=1)
        fetched_post_content = f'{post.content}'
        self.assertEquals(fetched_post_content, 'Hello, Test!')


class HomePageViewTest(TestCase):

    def setUp(self) -> None:
        Post.objects.create(content='Another test is coming!')
    
    def test_view_url_exists_at_proper_location(self) -> None:
        resp = self.client.get('/')
        self.assertEquals(resp.status_code, 200)

    def test_view_uses_correct_template(self) -> None:
        resp = self.client.get(reverse('home'))
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
