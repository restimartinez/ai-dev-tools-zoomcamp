from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.test import TestCase
from django.urls import reverse

from chores.models import FamilyMember

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


class FamilyMemberModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='alex',
            password='test-password-123',
        )

    def test_create_family_member_with_defaults(self):
        member = FamilyMember.objects.create(user=self.user)

        self.assertFalse(member.is_parent)
        self.assertTrue(member.is_active)
        self.assertEqual(member.display_name, '')
        self.assertEqual(member.user, self.user)
        self.assertEqual(self.user.family_member, member)

    def test_create_parent_family_member(self):
        member = FamilyMember.objects.create(
            user=self.user,
            is_parent=True,
            is_active=True,
            display_name='Alex (Parent)',
        )

        self.assertTrue(member.is_parent)
        self.assertTrue(member.is_active)
        self.assertEqual(member.display_name, 'Alex (Parent)')

    def test_get_display_name_uses_custom_name_when_set(self):
        member = FamilyMember.objects.create(
            user=self.user,
            display_name='Alex',
        )

        self.assertEqual(member.get_display_name(), 'Alex')
        self.assertEqual(str(member), 'Alex')

    def test_get_display_name_falls_back_to_username(self):
        member = FamilyMember.objects.create(user=self.user)

        self.assertEqual(member.get_display_name(), 'alex')
        self.assertEqual(str(member), 'alex')

    def test_user_can_have_only_one_family_member(self):
        FamilyMember.objects.create(user=self.user)

        with self.assertRaises(IntegrityError):
            FamilyMember.objects.create(user=self.user)

    def test_deactivated_member_remains_linked_to_user(self):
        member = FamilyMember.objects.create(user=self.user, is_active=True)
        member.is_active = False
        member.save()

        member.refresh_from_db()
        self.assertFalse(member.is_active)
        self.assertEqual(member.user.username, 'alex')
