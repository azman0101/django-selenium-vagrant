from django.core.urlresolvers import reverse
from django.test import Client, TestCase


class HelloTest(TestCase):
    def test_hello(self):
        client = Client()
        url = reverse('hello:basic_hello')
        response = client.get(url)
        self.assertEqual(
            200,
            response.status_code)
        self.assertIn(
            'Hello, you!',
            response.content)
