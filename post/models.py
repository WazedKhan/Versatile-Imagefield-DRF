from django.db import models
from django.contrib.auth.models import User

from versatileimagefield.fields import VersatileImageField, PPOIField


class Product(models.Model):
    name=models.CharField(max_length=255)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    image = VersatileImageField(
        "Image",
        upload_to="media/",
        ppoi_field="image_ppoi"
    )
    hero = VersatileImageField(
        "Hero",
        upload_to="media/",
        null=True, blank=True,
        ppoi_field="hero_ppoi"
    )
    image_ppoi = PPOIField()
    hero_ppoi = PPOIField()

    def __str__(self):
        return self.name
