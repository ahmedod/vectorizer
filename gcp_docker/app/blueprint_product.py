""" products bleuprints """
from product_management.product_management import create_product, list_products, get_product, update_product_labels, delete_product, \
     purge_orphan_products
from flask import Flask, request, jsonify, Blueprint, Response
from flasgger import swag_from
from flasgger import Swagger
import os
PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION")

product = Blueprint('product_v2', __name__, url_prefix='/v2/product')


@swag_from('./apidocs/product/create_product.yml')
@product.route('/create_product/<string:product_id>/product/<string:product_name>/category/<string:category>', methods=['POST'])
def create_product_f(product_id, product_name, category):
    """
    """
    try:
        result = create_product(
            PROJECT_ID, LOCATION, product_id, product_name, category)
        return jsonify(status=True, message='To-do saved successfully!', result=str(result)), 201
    except Exception as err:
        if "Invalid product categories" in str(err):
            return jsonify(error="Invalid product categories",
                           message="valid product categories are apparel, homegoods, toys, apparel-v2, homegoods-v2, toys-v2, packagedgoods-v1"), 400
        if "already exists" in str(err):
            return jsonify(error="AlreadyExists",
                           message="Product with ID {} already exists.".format(product_id)), 409
        raise Exception(str(err))


@swag_from('./apidocs/product/list_products.yml')
@product.route('/list_products', methods=['GET'])
def list_products_f():
    """
    """
    try:
        result = list_products(PROJECT_ID, LOCATION)
        return jsonify(status=True, message='To-do saved successfully!', result=str(result)), 201
    except Exception as err:
        raise Exception(str(err))


@swag_from('./apidocs/product/get_product.yml')
@product.route('/get_product/<string:product_id>', methods=['GET'])
def get_product_f(product_id):
    """
    """
    try: 
        result = get_product(PROJECT_ID, LOCATION, product_id)
        return jsonify(status=True, message='To-do saved successfully!', result=str(result)), 201
    except Exception as err:
        raise Exception(str(err))


@swag_from('./apidocs/product/update_product.yml')
@product.route('/update_product/<string:product_id>', methods=['POST'])
def update_product_f(product_id):
    """
    """
    try:
        infos = request.get_json()
        result = update_product_labels(PROJECT_ID, LOCATION, product_id, infos['key'], infos['value'])
        return jsonify(status=True, message='To-do saved successfully!', result=str(result)), 201
    except Exception as err:
        raise Exception(str(err))


@swag_from('./apidocs/product/delete_product.yml')
@product.route('/delete_product/<string:product_id>', methods=['DELETE'])
def delete_product_f(product_id):
    """
    """
    try:
        result = delete_product(PROJECT_ID, LOCATION, product_id)
        return jsonify(status=True, message='To-do saved successfully!', result=str(result)), 201
    except Exception as err:
        raise Exception(str(err))


@swag_from('./apidocs/product/delete_unassigned_product.yml')
@product.route('/delete_unassigned_product', methods=['DELETE'])
def delete_unassigned_product_f():
    """
    """
    try:
        result = purge_orphan_products(PROJECT_ID, LOCATION, force=True)
        return jsonify(status=True, message='To-do saved successfully!', result=str(result)), 201
    except Exception as err:
        raise Exception(str(err))
