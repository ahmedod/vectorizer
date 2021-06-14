""" product manegement module """ 
import argparse
from google.cloud import vision


def create_product(
        project_id, location, product_id, product_display_name,
        product_category):
    """Create one product.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_id: Id of the product.
        product_display_name: Display name of the product.
        product_category: Category of the product.
    """
    client = vision.ProductSearchClient()

    # A resource that represents Google Cloud Platform location.
    location_path = client.location_path(project=project_id, location=location)

    # Create a product with the product specification in the region.
    # Set product display name and product category.
    product = vision.types.Product(
        display_name=product_display_name,
        product_category=product_category)

    # The response is the product with the `name` field populated.
    response = client.create_product(
        parent=location_path,
        product=product,
        product_id=product_id)

    # Display the product information.
    print('Product name: {}'.format(response.name))
    return response
# [END vision_product_search_create_product]


# [START vision_product_search_list_products]
def list_products(project_id, location):
    """List all products.
    Args:
        project_id: Id of the project.
        location: A compute region name.
    """
    client = vision.ProductSearchClient()

    # A resource that represents Google Cloud Platform location.
    location_path = client.location_path(project=project_id, location=location)

    # List all the products available in the region.
    products = client.list_products(parent=location_path)
    result = []
    # Display the product information.
    for product in products:
        print('Product name: {}'.format(product.name))
        print('Product id: {}'.format(product.name.split('/')[-1]))
        print('Product display name: {}'.format(product.display_name))
        print('Product description: {}'.format(product.description))
        print('Product category: {}'.format(product.product_category))
        print('Product labels: {}\n'.format(product.product_labels))
        result.append({"Product name": str(product.name),
                       "Product id": str(product.name.split('/')[-1]),
                       "Product display name": str(product.display_name),
                       "Product description": str(product.description),
                       "Product category": str(product.product_category),
                       "Product labels": str(product.product_labels)})
    return str(result)
# [END vision_product_search_list_products]


# [START vision_product_search_get_product]
def get_product(project_id, location, product_id):
    """Get information about a product.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_id: Id of the product.
    """
    client = vision.ProductSearchClient()

    # Get the full path of the product.
    product_path = client.product_path(
        project=project_id, location=location, product=product_id)

    # Get complete detail of the product.
    product = client.get_product(name=product_path)
    result = []
    # Display the product information.
    print('Product name: {}'.format(product.name))
    print('Product id: {}'.format(product.name.split('/')[-1]))
    print('Product display name: {}'.format(product.display_name))
    print('Product description: {}'.format(product.description))
    print('Product category: {}'.format(product.product_category))
    print('Product labels: {}'.format(product.product_labels))
    result.append({"Product name": str(product.name),
                   "Product id": str(product.name.split('/')[-1]),
                   "Product display name": str(product.display_name),
                   "Product description": str(product.description),
                   "Product category": str(product.product_category),
                   "Product labels": str(product.product_labels)})
    return str(result)
# [END vision_product_search_get_product]


# [START vision_product_search_update_product_labels]
def update_product_labels(
        project_id, location, product_id, key, value):
    """Update the product labels.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_id: Id of the product.
        key: The key of the label.
        value: The value of the label.
    """
    client = vision.ProductSearchClient()

    # Get the name of the product.
    product_path = client.product_path(
        project=project_id, location=location, product=product_id)

    # Set product name, product label and product display name.
    # Multiple labels are also supported.
    key_value = vision.types.Product.KeyValue(key=key, value=value)
    product = vision.types.Product(
        name=product_path,
        product_labels=[key_value])

    # Updating only the product_labels field here.
    update_mask = vision.types.FieldMask(paths=['product_labels'])

    # This overwrites the product_labels.
    updated_product = client.update_product(
        product=product, update_mask=update_mask)

    # Display the updated product information.
    print('Product name: {}'.format(updated_product.name))
    print('Updated product labels: {}'.format(product.product_labels))
    return str({"Product name": str(updated_product.name),
            "Updated product labels": str(product.product_labels)})
# [END vision_product_search_update_product_labels]


# [START vision_product_search_delete_product]
def delete_product(project_id, location, product_id):
    """Delete the product and all its reference images.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_id: Id of the product.
    """
    client = vision.ProductSearchClient()

    # Get the full path of the product.
    product_path = client.product_path(
        project=project_id, location=location, product=product_id)

    # Delete a product.
    res = client.delete_product(name=product_path)
    print('Product deleted.')
    return str(res) #str('Product deleted.')
# [END vision_product_search_delete_product]


# [START vision_product_search_purge_orphan_products]
def purge_orphan_products(project_id, location, force):
    """Delete all products not in any product sets.
    Args:
        project_id: Id of the project.
        location: A compute region name.
    """
    client = vision.ProductSearchClient()

    parent = client.location_path(
        project=project_id, location=location)

    # The purge operation is async.
    operation = client.purge_products(
        parent=parent,
        delete_orphan_products=True,
        # The operation is irreversible and removes multiple products.
        # The user is required to pass in force=True to actually perform the
        # purge.
        # If force is not set to True, the service raises an exception.
        force=force)

    operation.result(timeout=120)

    print('Orphan products deleted.')
    return str('Orphan products deleted.')
# [END vision_product_search_purge_orphan_products]
