from django.test import TestCase
from django.urls import reverse


class TranslatorViewTests(TestCase):
    """Tests for views in the translator app."""

    def test_landing_page(self):
        """Landing view should return HTTP 200."""
        response = self.client.get(reverse("landing"))
        self.assertEqual(response.status_code, 200)

