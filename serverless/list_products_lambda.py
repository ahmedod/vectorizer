import os
import json
from google.cloud import vision
from google.cloud.vision import types


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"
project_id = os.getenv("PROJECT_ID")
location = os.getenv("LOCATION")


def lambda_handler(event, context):
    client = vision.ProductSearchClient()
    location_path = client.location_path(project=project_id, location=location)
    products = client.list_products(parent=location_path)
    result = []
    for product in products:
        result.append({"Product name": str(product.name),
                       "Product id": str(product.name.split('/')[-1]),
                       "Product display name": str(product.display_name),
                       "Product description": str(product.description),
                       "Product category": str(product.product_category),
                       "Product labels": str(product.product_labels)})
    eturn {"statusCode": 200, "body": json.dumps(result)}
