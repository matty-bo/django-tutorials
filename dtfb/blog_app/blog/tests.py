from blog.models import Post
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.


class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.post = Post.objects.create(
            author=self.user,
            title='Test title 1',
            body='Body for test 1')

    def test_string_representation(self):
        post = Post(title='whatever')
        self.assertEquals(str(post), post.title)

    def test_get_absolute_url(self):
        self.assertEquals(self.post.get_absolute_url(), '/post/1/')

    def test_post_content(self):
        self.assertEquals(f'{self.post.title}', 'Test title 1')
        self.assertEquals(f'{self.post.author}', 'testuser')
        self.assertEquals(f'{self.post.body}', 'Body for test 1')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Body for test 1')
        self.assertTemplateUsed('home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/10000/')
        self.assertEquals(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Test title 1')
        self.assertTemplateUsed('post_detail.html')

    def test_post_create_view(self):
        response = self.client.post(reverse('post_new'), {
            'title': 'New title',
            'body': 'New body',
            'author': self.user.id
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Post.objects.last().title, 'New title')
        self.assertEquals(Post.objects.last().body, 'New body')
        self.assertEquals(Post.objects.last().author.id, self.user.id)

    def test_post_update_view(self):
        response = self.client.post(reverse('post_edit', args='1'), {
            'title': 'Updated title',
            'body': 'Updated body'
        })
        self.assertEquals(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', args='1'))
        self.assertEquals(response.status_code, 302)
