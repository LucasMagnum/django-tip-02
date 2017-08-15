from django.core.management.base import BaseCommand
from products.models import Category, Product


class Command(BaseCommand):
    """This command was created to insert products and categories into database."""

    help = "Insert 500 products and 50 categories into database"

    def handle(self, *args, **options):
        self.stdout.write("Cleaning database...")
        Category.objects.all().delete()
        Product.objects.all().delete()

        self.stdout.write("Generating categories")
        categories = []

        for num in range(1, 51):
            # Is active will be False when the num is multiple of 5
            # This will generate 10 categories with the False flag
            is_active = num % 5 != 0
            categories.append(
                Category(name=f"category #{num}", is_active=is_active)
            )

        Category.objects.bulk_create(categories)

        self.stdout.write("Generating subcatories")

        # The first 5 catories will have 10 subcatories each
        for category in Category.objects.all()[:5]:
            subcategories = Category.objects.filter(id__gt=category.id * 10)
            category.subcategories = subcategories[:10]

        self.stdout.write("Generating products")

        products = []
        product_id = 1

        # Each category will have 10 products
        for category in Category.objects.all():
            for num in range(product_id * 10, (product_id * 10 + 10)):
                products.append(
                    Product(
                        title=f"product #{num}",
                        category=category
                    )
                )

            product_id += 1

        Product.objects.bulk_create(products)

        products_count = Product.objects.count()
        categories_count = Category.objects.count()

        self.stdout.write(
            self.style.SUCCESS(f'Inserted {products_count} products and {categories_count} categories')
        )
