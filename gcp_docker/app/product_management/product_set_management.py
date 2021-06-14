""" product management Modules """
import argparse
from google.cloud import vision

def create_product_set(project_id, location, product_set_id, product_set_display_name):
    """Create a product set.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_set_id: Id of the product set.
        product_set_display_name: Display name of the product set.
    """
    client = vision.ProductSearchClient()
    # A resource that represents Google Cloud Platform location.
    location_path = client.location_path(project=project_id, location=location)
    # Create a product set with the product set specification in the region.
    product_set = vision.types.ProductSet(display_name=product_set_display_name)
    # The response is the product set with `name` populated.
    response = client.create_product_set(
        parent=location_path,
        product_set=product_set,
        product_set_id=product_set_id)
    # Display the product set information.
    print('Product set name: {}'.format(response.name))
    return response
# [END vision_product_search_create_product_set]


# [START vision_product_search_list_product_sets]
def list_product_sets(project_id, location):
    """List all product sets.
    Args:
        project_id: Id of the project.
        location: A compute region name.
    """
    client = vision.ProductSearchClient()

    # A resource that represents Google Cloud Platform location.
    location_path = client.location_path(
        project=project_id, location=location)

    # List all the product sets available in the region.
    product_sets = client.list_product_sets(parent=location_path)
    results = []

    # Display the product set information.
    for product_set in product_sets:
        print('Product set name: {}'.format(product_set.name))
        print('Product set id: {}'.format(product_set.name.split('/')[-1]))
        print('Product set display name: {}'.format(product_set.display_name))
        print('Product set index time:')
        print('  seconds: {}'.format(product_set.index_time.seconds))
        print('  nanos: {}\n'.format(product_set.index_time.nanos))
        results.append({"Product set name": str(product_set.name),
                        "Product set id": str(product_set.name.split('/')[-1]),
                        "Product set display name": str(product_set.display_name),
                        "Product set index time: seconds": str(product_set.index_time.seconds),
                        "Product set index time: nanos": str(product_set.index_time.nanos)})
                
    return results
# [END vision_product_search_list_product_sets]


# [START vision_product_search_get_product_set]
def get_product_set(project_id, location, product_set_id):
    """Get info about the product set.
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

    # Get complete detail of the product set.
    product_set = client.get_product_set(name=product_set_path)

    # Display the product set information.
    print('Product set name: {}'.format(product_set.name))
    print('Product set id: {}'.format(product_set.name.split('/')[-1]))
    print('Product set display name: {}'.format(product_set.display_name))
    print('Product set index time:')
    print('  seconds: {}'.format(product_set.index_time.seconds))
    print('  nanos: {}'.format(product_set.index_time.nanos))
    result = {"Product set name": str(product_set.name),
              "Product set id": str(product_set.name.split('/')[-1]),
              "Product set display name": str(product_set.display_name),
              "Product set index time: seconds": str(product_set.index_time.seconds),
              "Product set index time: nanos": str(product_set.index_time.nanos)}
    return result
# [END vision_product_search_get_product_set]


# [START vision_product_search_delete_product_set]
def delete_product_set(project_id, location, product_set_id):
    """Delete a product set.
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

    # Delete the product set.
    client.delete_product_set(name=product_set_path)
    print('Product set deleted.')
    return 'Product set deleted.'
# [END vision_product_search_delete_product_set]
