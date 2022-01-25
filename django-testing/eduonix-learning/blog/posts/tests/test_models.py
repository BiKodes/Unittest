from audioop import reverse
from turtle import title

from django.http import response
from django.shortcuts import reverse
from django.test import  TestCase

from posts.models import Post


class PostTests(TestCase):

    @classmethod
    def setUp(cls):
        Post.objects.create(title='This is a test')

    def test_text(self):
        post = Post.objects.get(id=1)
        expected_post_title = post.title
        self.assertEquals(expected_post_title, 'This is a test')

    def test_post_list_view(self):
        response = self.client.get(reverse('posts'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'This is a test')
        self.assertTemplateUsed(response, 'posts.html')