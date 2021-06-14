""" reference set bleuprints"""
from product_management.reference_image_management import create_reference_image, list_reference_images, \
    get_reference_image, delete_reference_image
from flask import Flask, request, jsonify, Blueprint, Response
from flasgger import swag_from
from flasgger import Swagger

import os
PROJECT_ID = os.environ.get("PROJECT_ID")
LOCATION = os.environ.get("LOCATION")

#route to change
reference_set = Blueprint('reference_set_v2', __name__, url_prefix='/v2/reference_set')


@swag_from('./apidocs/reference_set/create_refrence_image.yml')
@reference_set.route('/create_refrence_image/<string:product_id>/<string:reference_image_id>', methods=['POST'])
def create_refrence_image_f(product_id, reference_image_id):
    """Create a reference image.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_id: Id of the product.
        reference_image_id: Id of the reference image.
        gcs_uri: Google Cloud Storage path of the input image.
    """
    try:
        infos = request.get_json()
        result = create_reference_image(PROJECT_ID, LOCATION, product_id, reference_image_id,  infos['gcs_uri'])
        return jsonify(status=True, message='To-do saved successfully!', result=result), 201
    except Exception as err:
        raise Exception(str(err))


@swag_from('./apidocs/reference_set/list_reference_image.yml')
@reference_set.route('/list_reference_image/<string:product_id>/', methods=['GET'])
def list_reference_image_f(product_id):
    """List all images in a product.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_id: Id of the product.
    """
    try:
        result = list_reference_images(PROJECT_ID, LOCATION, product_id)
        return jsonify(status=True, message='To-do saved successfully!', result=str(result)), 201
    except Exception as err:
        raise Exception(str(err))


@swag_from('./apidocs/reference_set/get_reference_image.yml')
@reference_set.route('/get_reference_image/<string:product_id>/<string:reference_image_id>', methods=['GET'])
def get_reference_image_f(product_id, reference_image_id):
    """Get info about a reference image.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_id: Id of the product.
        reference_image_id: Id of the reference image.
    """
    try:
        result = get_reference_image(PROJECT_ID, LOCATION, product_id, reference_image_id)
        return jsonify(status=True, message='To-do saved successfully!', result=str(result)), 201
    except Exception as err:
        raise Exception(str(err))


@swag_from('./apidocs/reference_set/delete_reference_image.yml')
@reference_set.route('/delete_reference_image/<string:product_id>/<string:reference_image_id>', methods=['DELETE'])
def delete_reference_image_f(product_id, reference_image_id):
    """Delete a reference image.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_id: Id of the product.
        reference_image_id: Id of the reference image.
    """
    try:
        result = delete_reference_image(PROJECT_ID, LOCATION, product_id, reference_image_id)
        return jsonify(status=True, message='To-do saved successfully!', result=str(result)), 201
    except Exception as err:
        raise Exception(str(err))