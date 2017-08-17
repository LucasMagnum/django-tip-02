from django.db.models import Prefetch

from .decorators import debugger_queries
from .models import Category, Product


def categories_list():
    categories_qs = Category.objects.all()

    categories = []

    for category in categories_qs:
        subcategories = [sub.name for sub in category.subcategories.all()]

        categories.append({
            'name': category.name,
            'is_active': category.is_active,
            'subcategories': subcategories
        })

    return categories


def debugger_categories_list():
    """Run debugger queries for categories_list function."""
    return debugger_queries(categories_list)()


def categories_list_prefetch_related():
    categories_qs = Category.objects.prefetch_related('subcategories')

    categories = []

    for category in categories_qs:
        subcategories = [sub.name for sub in category.subcategories.all()]

        categories.append({
            'name': category.name,
            'is_active': category.is_active,
            'subcategories': subcategories
        })

    return categories


def debugger_categories_list_prefetch_related():
    """Run debugger queries for categories_list_prefetch_related function."""
    return debugger_queries(categories_list_prefetch_related)()


def categories_list_active_subcategories():
    """Return all categories and list only the active subcatories."""
    categories_qs = Category.objects.prefetch_related("subcategories")

    categories = []

    for category in categories_qs:
        subcategories = [sub.name for sub in
                         category.subcategories.filter(is_active=True)]

        categories.append({
            'name': category.name,
            'is_active': category.is_active,
            'subcategories': subcategories
        })

    return categories


def debugger_categories_list_active_subcategories():
    """Run debugger queries for categories_list_active_subcategories."""
    return debugger_queries(categories_list_active_subcategories)()


def categories_list_active_subcategories_using_prefetch_attr():
    categories_qs = Category.objects.prefetch_related(
        Prefetch(
            'subcategories',
            queryset=Category.objects.filter(is_active=True),
            to_attr='active_subcategories'
        )
    )

    categories = []

    for category in categories_qs:
        subcategories = [sub.name for sub in category.active_subcategories]

        categories.append({
            'name': category.name,
            'is_active': category.is_active,
            'subcategories': subcategories
        })

    return categories


def debugger_categories_list_active_subcategories_using_prefetch_attr():
    return debugger_queries(categories_list_active_subcategories_using_prefetch_attr)()  # noqa


def categories_list_active_subcategories_using_prefetch_queryset():
    categories_qs = Category.objects.prefetch_related(
        Prefetch(
            'subcategories',
            queryset=Category.objects.filter(is_active=True),
        )
    )

    categories = []

    for category in categories_qs:
        subcategories = [sub.name for sub in category.subcategories.all()]

        categories.append({
            'name': category.name,
            'is_active': category.is_active,
            'subcategories': subcategories
        })

    return categories


def debugger_categories_list_active_subcategories_using_prefetch_queryset():
    return debugger_queries(categories_list_active_subcategories_using_prefetch_queryset)()  # noqa


def products_list():
    product_qs = Product.objects.all()

    products = []

    for product in product_qs:
        products.append({
            'id': product.id,
            'title': product.title,
            'category': product.category.name
        })

    return products


def debugger_products_list():
    """Run debugger queries for products_list function."""
    return debugger_queries(products_list)()


def products_list_select_related():
    product_qs = Product.objects.select_related('category').all()

    products = []

    for product in product_qs:
        products.append({
            'id': product.id,
            'title': product.title,
            'category': product.category.name
        })

    return products


def debugger_products_list_select_related():
    """Run debugger queries for products_list_select_related function."""
    return debugger_queries(products_list_select_related)()
