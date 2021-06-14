import os
import json
from google.cloud import vision
from google.cloud.vision import types


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"
project_id = os.getenv("PROJECT_ID")
location = os.getenv("LOCATION")


def lambda_handler(event, context):
    """ create a product
    """
    product_id = event["pathParameters"]['product_id']
    client = vision.ProductSearchClient()
    product_path = client.product_path(project=project_id, location=location, product=product_id) 
    response = client.delete_product(name=product_path)
    not_found = "item not found"
    delete_success = "item deleted successfully"
    if response is None:
        message = not_found
        code = 404
    else:
        message = delete_success
        code = 200

    return {"statusCode": code, "body": json.dumps(str(message))}
