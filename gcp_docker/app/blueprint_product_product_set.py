"""product product set bleuprints """
from product_management.product_in_product_set_management import add_product_to_product_set, list_products_in_product_set, \
    remove_product_from_product_set, purge_products_in_product_set

from flask import Flask, request, jsonify, Blueprint, Response
from flasgger import swag_from
from flasgger import Swagger
import os
PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION")

#from app import PROJECT_ID, LOCATION
# route to change
product_product_set = Blueprint('product_product_set_v2', __name__, url_prefix='/v2/product_product_set')



@swag_from('./apidocs/product_in_product_set/product_product_set_add.yml')
@product_product_set.route('/add_product_to_product_set', methods=['POST'])
def add_product_to_product_set_f():
    """Add a product to a product set.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_id: Id of the product.
        product_set_id: Id of the product set.
    """
    try:
        params = request.args.to_dict()
        result = add_product_to_product_set(PROJECT_ID, LOCATION, params["product_id"], params["product_set_id"])
        return jsonify(status=True, message='To-do saved successfully!', result=str(result)), 201
    except Exception as err:
        raise Exception(str(err))


@swag_from('./apidocs/product_in_product_set/product_product_set_list.yml')
@product_product_set.route('/list_products_in_product_set', methods=['GET'])
def list_products_in_product_set_f():
    """List all products in a product set.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_set_id: Id of the product set.
    """
    
    try:
        params = request.args.to_dict()
        result = list_products_in_product_set(PROJECT_ID, LOCATION, params['product_set_id'])
        return jsonify(status=True, message='To-do saved successfully!', result=str(result)), 201
    except Exception as err:
        raise Exception(str(err))


@swag_from('./apidocs/product_in_product_set/product_product_set_remove.yml')
@product_product_set.route('/remove_product_from_product_set', methods=['DELETE'])
def remove_product_from_product_set_f():
    """Remove a product from a product set.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_id: Id of the product.
        product_set_id: Id of the product set.
    """
    try:
        params = request.args.to_dict()
        result = remove_product_from_product_set(PROJECT_ID, LOCATION, params["product_id"], params["product_set_id"])
        return jsonify(status=True, message='To-do saved successfully!', result=str(result)), 201
    except Exception as err:
        raise Exception(str(err))


@swag_from('./apidocs/product_in_product_set/product_product_set_purge.yml')
@product_product_set.route('/purge_products_in_product_set', methods=['DELETE'])
def purge_products_in_product_set_f():
    """Delete all products in a product set.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_set_id: Id of the product set.
        force: Perform the purge only when force is set to True.
    """
    try:
        params = request.args.to_dict()
        result = purge_products_in_product_set(PROJECT_ID, LOCATION, params["product_set_id"], force=True)
        return jsonify(status=True, message='To-do saved successfully!', result=str(result)), 201
    except Exception as err:
        raise Exception(str(err))
