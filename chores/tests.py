from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class AuthenticationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='parent',
            password='test-password-123',
        )

    def test_anonymous_user_is_redirected_to_login(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, f"{reverse('login')}?next=/")

    def test_authenticated_user_can_view_home(self):
        self.client.login(username='parent', password='test-password-123')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome')
        self.assertContains(response, 'parent')

    def test_login_with_valid_credentials(self):
        response = self.client.post(
            reverse('login'),
            {'username': 'parent', 'password': 'test-password-123'},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('home'))

    def test_login_with_invalid_credentials(self):
        response = self.client.post(
            reverse('login'),
            {'username': 'parent', 'password': 'wrong-password'},
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'correct username and password')

    def test_logout_requires_post_and_redirects_to_login(self):
        self.client.login(username='parent', password='test-password-123')
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('login'))

        # Session cleared — home should require login again.
        home_response = self.client.get(reverse('home'))
        self.assertEqual(home_response.status_code, 302)
        self.assertTrue(home_response.url.startswith(reverse('login')))
