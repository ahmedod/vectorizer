import os, sys
from flask import Flask, request, jsonify, Blueprint, Response
from flask_pymongo import PyMongo
from flasgger import swag_from
from flasgger import Swagger
import requests
import json
import numpy as np


from blueprint_product_set import product_set
from blueprint_product import product
from blueprint_reference_set import reference_set
from blueprint_product_serach import product_search
from blueprint_product_product_set import product_product_set
from blueprint_import_product_set import import_product

blueprints = [product_set, product, reference_set, product_search, product_product_set, import_product]

application = Flask(__name__)
Swagger(application)


credential_path = "key.json"

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

for blueprint in blueprints:
    application.register_blueprint(blueprint)



if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    application.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
