# Generated by Django 3.2 on 2021-04-11 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='costumer',
            new_name='custumer',
        ),
    ]
