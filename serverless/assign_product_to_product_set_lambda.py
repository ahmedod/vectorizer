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
        product_id = event["queryStringParameters"]['product_id']
        product_set_id = event["queryStringParameters"]['product_set_id']
        client = vision.ProductSearchClient()
        product_set_path = client.product_set_path(project=project_id, location=location, product_set=product_set_id)
        product_path = client.product_path(project=project_id, location=location, product=product_id)
        client.add_product_to_product_set(name=product_set_path, product=product_path)
        message = "Product added to product set."
    except Exception as err:
        raise {"statusCode": 500, "body": json.dumps(str(err))}
    return {"statusCode": 200, "body": json.dumps(str(message))}
