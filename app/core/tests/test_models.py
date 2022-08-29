from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """ Test models. """
    def test_create_user_with_email_successful(self):
        """ Test if creating a user with email successful"""
        email = "test@example.com"
        password = "TestPass1234"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test if new emails are normalized upon user sign up."""
        sample_emails = [
            ['Test1@EXAMPLE.com', 'Test1@example.com'],
            ['test2@EXAMPLE.COM', 'test2@example.com'],
            ['test3@Example.com', 'test3@example.com'],
            ['Test4@example.COM', 'Test4@example.com'],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email=email, password='testpass')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'TestPass223')

    def test_create_super_user(self):

        user = get_user_model().objects.create_superuser(
            'test@example.com', 'testpass123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

