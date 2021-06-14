
""" items management module """
import argparse
from google.cloud import vision


def add_product_to_product_set(
        project_id, location, product_id, product_set_id):
    """Add a product to a product set.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_id: Id of the product.
        product_set_id: Id of the product set.
    """
    client = vision.ProductSearchClient()

    # Get the full path of the product set.
    product_set_path = client.product_set_path(
        project=project_id, location=location,
        product_set=product_set_id)

    # Get the full path of the product.
    product_path = client.product_path(
        project=project_id, location=location, product=product_id)

    # Add the product to the product set.
    client.add_product_to_product_set(
        name=product_set_path, product=product_path)
    print('Product added to product set.')
    return 'Product added to product set.'
# [END vision_product_search_add_product_to_product_set]


# [START vision_product_search_list_products_in_product_set]
def list_products_in_product_set(
        project_id, location, product_set_id):
    """List all products in a product set.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_set_id: Id of the product set.
    """
    client = vision.ProductSearchClient()

    # Get the full path of the product set.
    product_set_path = client.product_set_path(
        project=project_id, location=location,
        product_set=product_set_id)

    # List all the products available in the product set.
    products = client.list_products_in_product_set(name=product_set_path)
    result = []
    # Display the product information.
    for product in products:
        print('Product name: {}'.format(product.name))
        print('Product id: {}'.format(product.name.split('/')[-1]))
        print('Product display name: {}'.format(product.display_name))
        print('Product description: {}'.format(product.description))
        print('Product category: {}'.format(product.product_category))
        print('Product labels: {}'.format(product.product_labels))
        result.append({"Product name": product.name,
                       "Product id": product.name.split('/')[-1],
                       "Product display name": product.display_name,
                       "Product description": product.description,
                       "Product category": product.product_category,
                       "Product labels": product.product_labels})

    return result
# [END vision_product_search_list_products_in_product_set]


# [START vision_product_search_remove_product_from_product_set]
def remove_product_from_product_set(
        project_id, location, product_id, product_set_id):
    """Remove a product from a product set.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_id: Id of the product.
        product_set_id: Id of the product set.
    """
    client = vision.ProductSearchClient()

    # Get the full path of the product set.
    product_set_path = client.product_set_path(
        project=project_id, location=location,
        product_set=product_set_id)

    # Get the full path of the product.
    product_path = client.product_path(
        project=project_id, location=location, product=product_id)

    # Remove the product from the product set.
    client.remove_product_from_product_set(
        name=product_set_path, product=product_path)
    print('Product removed from product set.')
    return 'Product removed from product set.'
# [END vision_product_search_remove_product_from_product_set]


# [START vision_product_search_purge_products_in_product_set]
def purge_products_in_product_set(
        project_id, location, product_set_id, force):
    """Delete all products in a product set.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_set_id: Id of the product set.
        force: Perform the purge only when force is set to True.
    """
    client = vision.ProductSearchClient()

    parent = client.location_path(
        project=project_id, location=location)

    product_set_purge_config = vision.types.ProductSetPurgeConfig(
        product_set_id=product_set_id)

    # The purge operation is async.
    operation = client.purge_products(
        parent=parent,
        product_set_purge_config=product_set_purge_config,
        # The operation is irreversible and removes multiple products.
        # The user is required to pass in force=True to actually perform the
        # purge.
        # If force is not set to True, the service raises an exception.
        force=force)

    operation.result(timeout=120)

    print('Deleted products in product set.')
    return 'Deleted products in product set.'
# [END vision_product_search_purge_products_in_product_set]
