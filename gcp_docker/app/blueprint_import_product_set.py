"""import product set bleuprint """
from product_management.import_product_sets import import_product_sets
from flask import Flask, request, jsonify, Blueprint, Response
from flasgger import swag_from
from flasgger import Swagger
import os
PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION")


#route to change
import_product = Blueprint('import_product_v2', __name__, url_prefix='/v2/import_product')
@swag_from('./apidocs/import_product/import_product_sets.yml')
@import_product.route('/import_product_sets', methods=['POST'])
def import_product_sets_f():
    """Import images of different products in the product set.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        gcs_uri: Google Cloud Storage URI.
            Target files must be in Product Search CSV format.
    """
    try:
        infos = request.get_json()
        result = import_product_sets(PROJECT_ID, LOCATION, infos['gcs_uri'])
        return jsonify(status=True, message='To-do saved successfully!', result=str(result)), 201
    except Exception as err:
        raise Exception(str(err))
