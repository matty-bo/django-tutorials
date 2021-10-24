from django.test import TestCase
from django.urls.base import reverse
from .models import Book, Review
from django.contrib.auth import get_user_model


class BookTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='reviewuser',
            email='reviewuser@email.com',
            password='testpass123',
        )

        self.book = Book.objects.create(
            title='Book 1',
            author='Author 1',
            price=10.01
        )

        self.review = Review.objects.create(
            book=self.book,
            author=self.user,
            review='A brilliant review',
        )

    def test_book_listing(self):
        self.assertEquals(f'{self.book.title}', 'Book 1')
        self.assertEquals(f'{self.book.author}', 'Author 1')
        self.assertEquals(f'{self.book.price}', '10.01')

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Book 1')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_detail_view(self):
        no_response = self.client.get('/books/12345/')
        self.assertEquals(no_response.status_code, 404)

        response = self.client.get(self.book.get_absolute_url())
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Book 1')
        self.assertContains(response, 'A brilliant review')
        self.assertTemplateUsed('books/book_detail.html')
