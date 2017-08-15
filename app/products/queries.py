from .decorators import debugger_queries
from .models import Product


def product_list():
    product_qs = Product.objects.all()

    products = []

    for product in product_qs:
        products.append({
            'id': product.id,
            'title': product.title,
            'category': product.category.name
        })

    return products


def product_list_select_related():
    product_qs = Product.objects.select_related('category').all()

    products = []

    for product in product_qs:
        products.append({
            'id': product.id,
            'title': product.title,
            'category': product.category.name
        })

    return products


def debugger_product_list():
    """Run debugger queries for product_list function."""
    return debugger_queries(product_list)()


def debugger_product_list_select_related():
    """Run debugger queries for product_list_select_related function."""
    return debugger_queries(product_list_select_related)()
