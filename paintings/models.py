import uuid
from django.db import models
from django.urls import reverse


class Painting(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    artwork_type = models.CharField(max_length=200, default='acrylic')
    image = models.ImageField(upload_to='images/', blank=True)

    class Meta:
        permissions = [
            ('special_status', 'Purchased a painting'),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('painting_detail', args=[str(self.id)])
