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
    product_id = event["queryStringParameters"]['product_id']
    product_display_name = event["queryStringParameters"]['product_name']
    product_category = event["queryStringParameters"]['category']
    client = vision.ProductSearchClient()
    location_path = client.location_path(project=project_id, location=location)  
    product = vision.types.Product(display_name=product_display_name, product_category=product_category)
    response = client.create_product(parent=location_path, product=product, product_id=product_id)
    return {"statusCode": 200, "body": json.dumps(response)}
