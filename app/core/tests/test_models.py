"""
Tests for models.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_email(self):
        """Test creating a user with email"""
        email = "test@example.com"
        password = "testpass@123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users."""
        sample_emails = [
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["Test1@Example.com", "Test1@example.com"],
            ["TEST3@Example.com", "TEST3@example.com"],
            ["test4@Example.COM", "test4@example.com"],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample@123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email(self):
        """Test that creating user without email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'sample@123')

    def test_create_superuser(self):
        """Test to create superuser"""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
