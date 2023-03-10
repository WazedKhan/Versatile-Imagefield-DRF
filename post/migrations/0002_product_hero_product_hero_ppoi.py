# Generated by Django 4.1.4 on 2022-12-16 06:49

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="hero",
            field=versatileimagefield.fields.VersatileImageField(
                blank=True, null=True, upload_to="media/", verbose_name="Hero"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="hero_ppoi",
            field=versatileimagefield.fields.PPOIField(
                default="0.5x0.5", editable=False, max_length=20
            ),
        ),
    ]
