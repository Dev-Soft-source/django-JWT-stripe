from django.apps import AppConfig
import os

class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'

    def ready(self):
        if os.environ.get('DJANGO_ENV') == 'development':
            from . import seed_products
            seed_products.create_seed_products()

