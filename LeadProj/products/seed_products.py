# accounts/seed_products.py

from accounts.models import User
from products.models import Category, Product
import logging

logger = logging.getLogger(__name__)

def create_seed_products():
    categories = [
        {
            'name': 'Electronics',
            'description': 'Electronic devices and gadgets'
        },
        {
            'name': 'Clothing',
            'description': 'Apparel and clothing items'
        },
        {
            'name': 'Home & Kitchen',
            'description': 'Home appliances and kitchenware'
        },
        {
            'name': 'Books',
            'description': 'Fiction and non-fiction books'
        },
        {
            'name': 'Toys',
            'description': 'Fun and educational toys for kids'
        },
    ]

    for c in categories:
        if not Category.objects.filter(name=c['name']).exists():
            category = Category.objects.create(**c)
            logger.info(f"[Seed] Created category: {category.name}")

    products = [
        {
            'name': 'Smartphone',
            'description': 'Latest model smartphone',
            'price': 699.99,
            'stock_quantity': 50,
            'category': Category.objects.get(name='Electronics'),
            'image': 'path/to/smartphone_image.jpg'
        },
        {
            'name': 'T-Shirt',
            'description': 'Cotton t-shirt with logo',
            'price': 19.99,
            'stock_quantity': 100,
            'category': Category.objects.get(name='Clothing'),
            'image': 'path/to/tshirt_image.jpg'
        },
        {
            'name': 'Blender',
            'description': 'High-speed blender for smoothies',
            'price': 89.99,
            'stock_quantity': 30,
            'category': Category.objects.get(name='Home & Kitchen'),
            'image': 'path/to/blender_image.jpg'
        },
        {
            'name': 'Smartphone XYZ',
            'description': 'A high-end smartphone with a 6.5-inch display, 128GB storage, and a 48MP camera.',
            'price': 799.99,
            'stock_quantity': 50,
            'category': Category.objects.get(name='Electronics'),
            'image': 'path/to/smartphonexyz_image.jpg'
        },
        {
            'name': 'Laptop ABC',
            'description': 'A sleek laptop with an Intel Core i7 processor, 16GB RAM, and 512GB SSD.',
            'price': 1299.99,
            'stock_quantity': 30,
            'category': Category.objects.get(name='Electronics'),
            'image': 'path/to/laptop_image.jpg'
        },
        {
            'name': 'T-shirt - Large',
            'description': 'A comfortable cotton t-shirt in a variety of colors, size large.',
            'price': 19.99,
            'stock_quantity': 100,
            'category': Category.objects.get(name='Clothing'),
            'image': 'path/to/tshirt_image.jpg'
        },
        {
            'name': 'Kitchen Blender',
            'description': 'A high-power blender for smoothies and soups with multiple speed settings.',
            'price': 89.99,
            'stock_quantity': 25,
            'category': Category.objects.get(name='Home & Kitchen'),
            'image': 'path/to/blender_image.jpg'
        },
        {
            'name': "Harry Potter and the Sorcerer's Stone",
            'description': "A novel by J.K. Rowling, the first book in the Harry Potter series.",
            'price': 14.99,
            'stock_quantity': 200,
            'category': Category.objects.get(name='Books'),
            'image': "path/to/harry_potter_book_image.jpg"
        },
        {
            'name': "Lego Building Set",
            'description': "A fun and educational Lego set for children ages 6-12, with over 500 pieces.",
            'price': 59.99,
            'stock_quantity': 150,
            'category': Category.objects.get(name='Toys'),
            'image': "path/to/lego_set_image.jpg"
        },        
    ]

    for p in products:
        if not Product.objects.filter(name=p['name']).exists():
            product = Product.objects.create(**p)
            logger.info(f"[Seed] Created product: {product.name}")
