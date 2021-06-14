""" product set bleuprints"""
from product_management.product_set_management import create_product_set, list_product_sets, get_product_set, delete_product_set
from flask import Flask, request, jsonify, Blueprint, Response
from flasgger import swag_from
from flasgger import Swagger
import os
PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION")

#route to change
product_set = Blueprint('product_set_v2', __name__, url_prefix='/v2/product_set')


@swag_from('./apidocs/product_set/create_product_set.yml')
@product_set.route('/create_product_set/<string:product_id>', methods=['POST'])
def create_product_set_f(product_id):
    """Create a product set.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_set_id: Id of the product set.
        product_set_display_name: Display name of the product set.
    """
    try:
        params = request.args.to_dict()
        result = create_product_set(PROJECT_ID, LOCATION, product_id, params['product_name'])
        return jsonify(status=True, message='To-do saved successfully!', result=str(result)), 201
    except Exception as err:
        raise Exception(str(err))


@swag_from('./apidocs/product_set/list_product_sets.yml')
@product_set.route('/list_product_sets', methods=['GET'])
def list_product_sets_f():
    """List all product sets.
    Args:
        project_id: Id of the project.
        location: A compute region name.
    """

    try:
        result = list_product_sets(PROJECT_ID, LOCATION)
        return jsonify(status=True, message='To-do saved successfully!', result=str(result)), 201
    except Exception as err:
        raise Exception(str(err))

@swag_from('./apidocs/product_set/get_product_set_info.yml')
@product_set.route('/get_product_set_info/<string:product_set_id>', methods=['GET'])
def get_product_set_f(product_set_id):
    """Get info about the product set.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_set_id: Id of the product set.
    """
    try:
        result = get_product_set(PROJECT_ID, LOCATION, product_set_id)
        return jsonify(status=True, message='To-do saved successfully!', result=str(result)), 201
    except Exception as err:
        raise Exception(str(err))


@swag_from('./apidocs/product_set/delete_product_set.yml')
@product_set.route('/delete_product_set/<string:product_id>', methods=['DELETE'])
def delete_product_set_f(product_id):
    """Delete a product set.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_set_id: Id of the product set.
    """

    try:
        result = delete_product_set(PROJECT_ID, LOCATION, product_id)
        return jsonify(status=True, message='To-do saved successfully!', result=str(result)), 201
    except Exception as err:
        raise Exception(str(err))