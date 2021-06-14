#!/usr/bin/env python
import argparse
from google.cloud import vision


# [START vision_product_search_create_reference_image]
def create_reference_image(
        project_id, location, product_id, reference_image_id, gcs_uri):
    """Create a reference image.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_id: Id of the product.
        reference_image_id: Id of the reference image.
        gcs_uri: Google Cloud Storage path of the input image.
    """
    client = vision.ProductSearchClient()

    # Get the full path of the product.
    product_path = client.product_path(
        project=project_id, location=location, product=product_id)

    # Create a reference image.
    reference_image = vision.types.ReferenceImage(uri=gcs_uri)

    # The response is the reference image with `name` populated.
    image = client.create_reference_image(
        parent=product_path,
        reference_image=reference_image,
        reference_image_id=reference_image_id)

    # Display the reference image information.
    result = {"Reference image name": image.name,
              "Reference image uri": image.uri}
    print('Reference image name: {}'.format(image.name))
    print('Reference image uri: {}'.format(image.uri))
    return result
# [END vision_product_search_create_reference_image]


# [START vision_product_search_list_reference_images]
def list_reference_images(
        project_id, location, product_id):
    """List all images in a product.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_id: Id of the product.
    """
    client = vision.ProductSearchClient()

    # Get the full path of the product.
    product_path = client.product_path(
        project=project_id, location=location, product=product_id)

    # List all the reference images available in the product.
    reference_images = client.list_reference_images(parent=product_path)

    # Display the reference image information.
    result = []
    for image in reference_images:
        print('Reference image name: {}'.format(image.name))
        print('Reference image id: {}'.format(image.name.split('/')[-1]))
        print('Reference image uri: {}'.format(image.uri))
        print('Reference image bounding polygons: {}'.format(
            image.bounding_polys))
        result.append({"Reference image name": image.name,
                       "Reference image id": image.name.split('/')[-1],
                       "Reference image uri": image.uri})
    return result
# [END vision_product_search_list_reference_images]


# [START vision_product_search_get_reference_image]
def get_reference_image(
        project_id, location, product_id, reference_image_id):
    """Get info about a reference image.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_id: Id of the product.
        reference_image_id: Id of the reference image.
    """
    client = vision.ProductSearchClient()

    # Get the full path of the reference image.
    reference_image_path = client.reference_image_path(
        project=project_id, location=location, product=product_id,
        reference_image=reference_image_id)

    # Get complete detail of the reference image.
    image = client.get_reference_image(name=reference_image_path)

    # Display the reference image information.
    result = {"Reference image name":image.name,
              "Reference image id": image.name.split('/')[-1],
              "Reference image uri": image.uri}
    print('Reference image name: {}'.format(image.name))
    print('Reference image id: {}'.format(image.name.split('/')[-1]))
    print('Reference image uri: {}'.format(image.uri))
    print('Reference image bounding polygons: {}'.format(image.bounding_polys))
    return result
# [END vision_product_search_get_reference_image]


# [START vision_product_search_delete_reference_image]
def delete_reference_image(
        project_id, location, product_id, reference_image_id):
    """Delete a reference image.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_id: Id of the product.
        reference_image_id: Id of the reference image.
    """
    client = vision.ProductSearchClient()

    # Get the full path of the reference image.
    reference_image_path = client.reference_image_path(
        project=project_id, location=location, product=product_id,
        reference_image=reference_image_id)

    # Delete the reference image.
    client.delete_reference_image(name=reference_image_path)
    print('Reference image deleted from product.')
    return 'Reference image deleted from product.'
# [END vision_product_search_delete_reference_image]

