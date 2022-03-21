from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

from .forms import CustomUserCreationForm
from .views import RegistrationPageView

class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='mike',
            email='mike@email.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'mike')
        self.assertEqual(user.email, 'mike@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


    def test_create_superuser(self):

        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@email.com',
            password='testpass123'
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_staff)


class RegistrationPageTests(TestCase):

    def setUp(self):
        url = reverse('register')
        self.response = self.client.get(url)

    def test_registration_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'register.html')
        self.assertContains(self.response, 'Register')
        self.assertNotContains(
            self.response, 'Hi there, I should not be on this page!')

    def test_registration_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_registration_view(self):
        view = resolve('/accounts/register/')
        self.assertEqual(
            view.func.__name__,
            RegistrationPageView.as_view().__name__
        )
