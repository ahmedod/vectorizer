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
        parent = client.location_path(project=project_id, location=location)
        product_set_purge_config = vision.types.ProductSetPurgeConfig(product_set_id=product_set_id)
        operation = client.purge_products(parent=parent, product_set_purge_config=product_set_purge_config, force=True)
        operation.result(timeout=120)
        message = "Deleted products in product set."
    except Exception as err:
        raise {"statusCode": 500, "body": json.dumps(str(err))}
    return {"statusCode": 200, "body": json.dumps(str(message))}
