from rest_framework import serializers

from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Serializes Person instances"""
    image = VersatileImageFieldSerializer(
        sizes=[
            ('orgnizal_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
            ('square_crop', 'crop__400x400'),
            # ('small_square_crop', 'crop__50x50')
        ]
    )
    hero = VersatileImageFieldSerializer(
        sizes=[
            ('orgnizal_size', 'url'),
            ('thumbnail', 'thumbnail__1024x250'),
            # ('square_crop', 'crop__400x400'),
            # ('small_square_crop', 'crop__50x50')
        ]
    )

    class Meta:
        model = Product
        fields = (
            'name',
            'image',
            'hero'
        )

    def create(self, validated_data):
        return Product.objects.create(
            user = self.context['request'].user,
            **validated_data
            )