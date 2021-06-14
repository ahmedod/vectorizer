import os
import json
from google.cloud import vision
from google.cloud.vision import types


class Exception(BaseException):
    pass


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"
project_id = os.getenv("PROJECT_ID")
location = os.getenv("LOCATION")


def lambda_handler(event, context):
    """ create a product
    """
    try:
        product_set_id = event["queryStringParameters"]['product_set_id']
        client = vision.ProductSearchClient()
        product_set_path = client.product_set_path(project=project_id, location=location, product_set=product_set_id)
        products = client.list_products_in_product_set(name=product_set_path)
        result = []
        for product in products:
            result.append({"Product name": product.name,
                           "Product id": product.name.split('/')[-1],
                           "Product display name": product.display_name,
                           "Product description": product.description,
                           "Product category": product.product_category,
                           "Product labels": product.product_labels})
    except Exception as err:
        raise {"statusCode": 500, "body": json.dumps(str(err))}
    return {"statusCode": 200, "body": json.dumps(result)}
