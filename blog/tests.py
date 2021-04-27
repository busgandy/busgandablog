from django.test import TestCase
from .models import Post
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your tests here.


class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='secret'
        )

        self.post = Post.objects.create(
            title='A good title',
            body='Nice body',
            author=self.user
        )

    def test_string_representation(self):
        post = Post(title='A good title')
        self.assertEqual(str(post), self.post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_views(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(no_response.status_code, 404)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')


    def test_post_update_view(self):
        response = self.client.get('/post/1/edit/')
        no_response = self.client.get('/post/100000/edit')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 301)


    def test_post_delete_view(self):
        response = self.client.get('/post/1/delete/')
        no_response = self.client.get('/post/100000/delete')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 301)

