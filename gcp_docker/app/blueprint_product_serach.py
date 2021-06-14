""" product search bleuprints """
from product_management.product_search import get_similar_products_file, get_similar_products_uri
from flask import Flask, request, jsonify, Blueprint, Response
from flasgger import swag_from
from flasgger import Swagger
from werkzeug import secure_filename

import os
PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION")


#route to change
product_search = Blueprint('product_search_v2', __name__, url_prefix='/v2/product_search')


@swag_from('./apidocs/product_search/get_similar_products_file.yml')
@product_search.route('/get_similar_products/file', methods=['POST'])
def get_similar_products_file_f():
    """Search similar products to image.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_set_id: Id of the product set.
        product_category: Category of the product.
        file_path: Local file path of the image to be searched.
        filter: Condition to be applied on the labels.
        Example for filter: (color = red OR color = blue) AND style = kids
        It will search on all products with the following labels:
        color:red AND style:kids
        color:blue AND style:kids
    """
    try:
        f=request.files['filename']
        f.save(secure_filename(f.filename))
        params = request.args.to_dict()


        result = get_similar_products_file(PROJECT_ID, LOCATION, params["product_set_id"],
                                           params["product_category"], f.filename, params["filters"])
        return jsonify(status=True, message='To-do saved successfully!', result=str(result)), 201
    except Exception as err:
        raise Exception(str(err))


@swag_from('./apidocs/product_search/get_similar_products_uri.yml')
@product_search.route('/get_similar_products/uri', methods=['POST'])
def get_similar_products_uri_f():
    """Search similar products to image.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_set_id: Id of the product set.
        product_category: Category of the product.
        file_path: Local file path of the image to be searched.
        filter: Condition to be applied on the labels.
        Example for filter: (color = red OR color = blue) AND style = kids
        It will search on all products with the following labels:
        color:red AND style:kids
        color:blue AND style:kids
    """
    try:
        params = request.args.to_dict()
        infos = request.get_json()
        result = get_similar_products_uri(PROJECT_ID, LOCATION, params["product_set_id"],
                                          params["product_category"], infos["gcs_uri"], params["filters"])
        return jsonify(status=True, message='To-do saved successfully!', result=str(result)), 201
    except Exception as err:
        raise Exception(str(err))
