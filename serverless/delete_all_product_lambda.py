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
    client = vision.ProductSearchClient()
    parent = client.location_path(project=project_id, location=location)

    # The purge operation is async.
    operation = client.purge_products(parent=parent, delete_orphan_products=True, force=True)
    operation.result(timeout=120)
    messsage = "puge success"
    return {"statusCode": 200, "body": json.dumps(messsage)}
