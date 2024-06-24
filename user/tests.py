from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
import logging

logger = logging.getLogger(__name__)
User = get_user_model()

class LoginViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword')

    def test_login_with_username(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome testuser! You have successfully logged in!')

    def test_login_with_email(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser@example.com',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome testuser! You have successfully logged in!')

    def test_login_invalid_credentials(self):
        response = self.client.post(reverse('login'), {
            'username': 'wronguser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)  # Assuming it redirects back to login page with errors
        self.assertContains(response, 'Invalid username/email or password')

    def test_login_error_logging(self):
        try:
            response = self.client.post(reverse('login'), {
                'username': 'wronguser',
                'password': 'wrongpassword'
            })
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, 'Invalid username/email or password')
        except Exception as e:
            logger.error(f"Error during login test: {e}")
            self.fail(f"Login test failed due to unexpected error: {e}")

