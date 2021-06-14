import os
import json
from google.cloud import vision
from google.cloud.vision import types


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"
project_id = os.getenv("PROJECT_ID")
location = os.getenv("LOCATION")


def lambda_handler(event, context):
    client = vision.ProductSearchClient()
    product_id = event["queryStringParameters"]['product_id']
    product_path = client.product_path(project=project_id, location=location, product=product_id)
    product = client.get_product(name=product_path)
    result = []
    result.append({"Product name": str(product.name),
                   "Product id": str(product.name.split('/')[-1]),
                   "Product display name": str(product.display_name),
                   "Product description": str(product.description),
                   "Product category": str(product.product_category),
                   "Product labels": str(product.product_labels)})
    resp = {"statusCode": 200, "headers": {"Access-Control-Allow-Origin": "*"}, "body": result}
    return resp
