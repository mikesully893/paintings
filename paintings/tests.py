from django.test import Client, TestCase
from django.urls import reverse

from .models import Painting


class PaintingTests(TestCase):

    def setUp(self):
        self.painting = Painting.objects.create(
            title='Mona Lisa',
            artist='Leonardo Da Vinci',
            price='1000.00',
        )

    def test_painting_listing(self):
        self.assertEqual(f"{self.painting.title}", "Mona Lisa")
        self.assertEqual(f"{self.painting.artist}", "Leonardo Da Vinci")
        self.assertEqual(f"{self.painting.price}", '1000.00')

    def test_painting_list_view(self):
        response = self.client.get(reverse('painting_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Mona Lisa')
        self.assertTemplateUsed(response, 'paintings/painting_list.html')

    def test_painting_detail_view(self):
        response = self.client.get(self.painting.get_absolute_url())
        no_response = self.client.get('/paintings/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Mona Lisa')
        self.assertTemplateUsed(response, 'paintings/painting_detail.html')
